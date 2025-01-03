import numpy as np

def sawtooth(t):
  return 2*t/(2*np.pi) - 1

def triangle(t):
  return 2*abs(sawtooth(t)) - 1

def play_ndarray_simpleaudio(y, sample_rate):
  """
    y: ndarray, float values between -1 and 1, shape (#samples,#channels), or only (#samples,) for mono sound
    sample_rate: sample rate in Hz
  """

  import simpleaudio as sa

  channels = 1 if y.ndim<2 else y.shape[-1]
  y = (y*32767).astype(np.int16).ravel()

  play_obj = sa.play_buffer(y.ravel(), channels, 2, sample_rate)
  play_obj.wait_done()

def play_ndarray_gst(y, sample_rate):
  """
    y: ndarray, float values between -1 and 1, shape (#samples,#channels), or only (#samples,) for mono sound
    sample_rate: sample rate in Hz
  """

  import gi, sys
  gi.require_version('Gst', '1.0')
  from gi.repository import Gst, GObject
  Gst.init(None)

  pipeline = Gst.Pipeline()

  appsrc = Gst.ElementFactory.make('appsrc', 'appsrc')
  queueaudio = Gst.ElementFactory.make('queue', 'queueaudio')
  audioconvert = Gst.ElementFactory.make('audioconvert', 'audioconvert')
  sink = Gst.ElementFactory.make('autoaudiosink', 'sink')

  appsrc.set_property("format", Gst.Format.TIME)
  appsrc.set_property("block", True)
  appsrc.set_property("is-live", True)
  channels = 1 if y.ndim<2 else y.shape[-1]
  appsrc.set_property("caps", Gst.Caps.from_string("audio/x-raw,format={},rate={},channels={},layout=interleaved".format("S16LE" if sys.byteorder=="little" else "S16BE", sample_rate, channels)))

  pipeline.add(appsrc)
  pipeline.add(queueaudio)
  pipeline.add(audioconvert)
  pipeline.add(sink)

  appsrc.link(queueaudio)
  queueaudio.link(audioconvert)
  audioconvert.link(sink)

  pipeline.set_state(Gst.State.PLAYING)

  y = (y*32767).astype(np.int16).ravel()
  appsrc.emit('push-buffer', Gst.Buffer.new_wrapped(y.tobytes()))
  appsrc.emit("end-of-stream")

  mainloop = GObject.MainLoop()

  bus = pipeline.get_bus()
  bus.add_signal_watch()
  def eos_callback(*args):
    pipeline.set_state(Gst.State.NULL)
    mainloop.quit()
  bus.connect("message::eos", eos_callback)

  mainloop.run()

def read_ndarrays_gst(sample_rate, device=None):
  """
  example:
    q, _ = simplebeep.functions.read_ndarrays_gst(44100)
    while True:
      print(q.get())
      q.task_done()

  setting device="alsa_output.pci-0000_00_1b.0.analog-stereo.monitor" will make it read from monitor instead of microphone
  """

  import gi, sys, queue
  gi.require_version('Gst', '1.0')
  from gi.repository import Gst, GObject, GstApp

  Gst.init(None)

  q = queue.Queue()

  pipeline = Gst.parse_launch("pulsesrc name=pulsesrc ! audioconvert ! audio/x-raw,format={},rate={},channels=1,layout=interleaved ! appsink name=sink emit-signals=true".format("S16LE" if sys.byteorder=="little" else "S16BE", sample_rate))

  if device is not None:
    pipeline.get_by_name("pulsesrc").set_property("device", device)

  def sample_callback(app_sink):
    buf = app_sink.pull_sample().get_buffer()

    success, map_info = buf.map(Gst.MapFlags.READ)
    arr = np.ndarray(shape=(buf.get_size()//2,), dtype=np.int16, buffer=map_info.data)
    buf.unmap(map_info)

    q.put(arr)

    return False

  pipeline.get_by_name("sink").connect("new-sample", sample_callback)

  pipeline.set_state(Gst.State.PLAYING)

  return q, pipeline

try:
  import gi, sys
  gi.require_version('Gst', '1.0')
  from gi.repository import Gst, GObject
  Gst.init(None)
  play_ndarray = play_ndarray_gst
except:
  import simpleaudio as sa
  play_ndarray = play_ndarray_simpleaudio

def beep(pitch=0, duration=.1, level=0, waveform=triangle, backend=play_ndarray):
  """
    pitch: 0 is concert pitch (A, 440 Hz), 1 is one half tone above, etc. (default: 0)
    duration: duration in seconds (default: 0.1 seconds)
    level: 0=maximum volume, -10=reduced by 10 dB, ... (default: 0)
    waveform: must be a function defined on interval [0, 2*pi]. minimum value -1, maximum value 1 (default: simplebeep.triangle)
    backend: either simplebeep.play_ndarray_gst or simplebeep.play_ndarray_simpleaudio. Omit for default.
  """

  sample_rate = 44100
  t = np.arange(0, duration, 1/sample_rate)
  frequency = 440 * 2**(pitch/12)
  period = 1/frequency
  y = waveform(np.mod(2*np.pi*t/period, 2*np.pi)) * 10**(level/10)
  backend(y, sample_rate)
