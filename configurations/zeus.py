from pybricks.parameters import Port, Direction, Color

from runs.chickenRun import ChickenRun
from runs.cameraRun import CameraRun
from runs.mixerRun import MixerRun
from runs.dragonRun import DragonRun
from runs.runBack import RunBack
from runs.cameraRun2 import CameraRun2
from runs.stageRun import StageRun
from runs.finalRun import FinalRun

from modules.components.drivebase import DriveBaseFull
from modules.components.lightSensor import LightSensor
from modules.components.menuSelector import MenuSelector, Col
from modules.components.gyro import Gyro
from modules.components.tools import RunState, Timer
from modules.components.motor import Motor

from modules.load_config import config


class zeus(config):
    def hydroRunResetArm(self):
        self.RMmotor.run_time(300, 400)

    def __init__(self):
        super().__init__()
        self.SPEED_LIST_COUNT = 2000
        self.ACCELERATION = 520
        self.STARTSPEED = 70
        self.TURN_SPEED_MIN = 40
        self.TURN_SPEED_MAX = 260
        self.LIGHTCAL_CONF = "zeus.cal"

        self.Lmotor = self.init(
            Motor, Port.A, self, Direction.COUNTERCLOCKWISE)
        self.Rmotor = self.init(
            Motor, Port.C, self, Direction.COUNTERCLOCKWISE)
        self.LMmotor = self.init(Motor, Port.B, self)
        self.RMmotor = self.init(Motor, Port.D, self)

        # self.runButton = runButton(TouchSensor(Port))
        self.gyro = self.init(Gyro, Port.S4, Direction.CLOCKWISE, self)
        self.Llight = self.init(LightSensor, Port.S2)
        self.Rlight = self.init(LightSensor, Port.S1)

        self.menuSelector = self.init(MenuSelector, Port.S3, [
                                      Col([7, 10, 19]), Col([77, 52, 31]), Col([54, 14, 24]), Col([9, 31, 30]), Col([34, 41, 85]), Col([27, 47, 31]), Col([11, 24, 96]), Col([85, 87, 100])], Col([9, 4, 16]), self.state)
        self.useMenuSelector = True
        self.leftpage = "runs"

        # self.lift = forklift(self, motor(self,
        #                                  Port.D, gears=[[12, 20], [28, 20], [8, 40]]), 110)

        self.drive = DriveBaseFull(self, self.Lmotor, self.Rmotor, self.gyro,
                                   56, 104, Llight=self.Llight, Rlight=self.Rlight)

        self.menu = {
            "runs": [ChickenRun(self), CameraRun(self), MixerRun(self), DragonRun(self), CameraRun2(self),  RunBack(self), StageRun(self), FinalRun(self)],
            "left": [None, self.resetCamerRunArm, None, self.resetDragonRunArm, None, None, self.resetStageRunArm, self.resetFinalRunArm],
            "utility": [self.drive.lightCal, self.gyro.calibrate, self.drive.tyreClean, self.drive.blank],
            "utility_name": ["LightCal", "gyroCal", "tyreClean", "blank"],
            "pages": ["runs", "utility"]
        }

        self.display = [self.drive.getHead, self.menuSelector.color]
        self.stopList = [self.drive, self.LMmotor, self.RMmotor]

        # self.xlift = forklift(Motor(Port.B))
        # self.ylift = forklift(Motor(Port.C))
        # self.lift = doubleForklift(self.xlift, self.ylift)
    def resetStageRunArm(self):
        self.LMmotor.run_time(-200, 1000)
    
    def resetDragonRunArm(self):
        self.RMmotor.run_time(100, 1000)
    
    def resetCamerRunArm(self):
        self.LMmotor.run_time(100, 1000)
    
    def resetFinalRunArm(self):
        self.LMmotor.run_time(300, 1000)