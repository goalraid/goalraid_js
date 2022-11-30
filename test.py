from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av

class VideoProcessor:
    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")


        return frame.av.VideoFrame.from_ndarray(frm, format='bgr24')


webrtc_streamer(key="key", video_processor_factory=VideoProcessor)
