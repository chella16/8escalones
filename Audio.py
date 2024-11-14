from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
class Audio():
    def __init__(self):
        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setSource(QUrl.fromLocalFile("TpFinal\Sounds\A.mp3"))  # Cambia a la ruta de tu archivo MP3
        self.audioOutput.setVolume(0.5)
        self.mediaPlayer.play()
    
    def cambiarVol(self, vol): 
        
        if vol == 0: 
            self.audioOutput.setVolume(0)
        else:
            self.audioOutput.setVolume(vol*0.01) 