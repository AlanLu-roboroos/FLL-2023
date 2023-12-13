from threading import Thread
from pybricks.tools import StopWatch

class FinalRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.Llight = config.Llight
        self.Rlight = config.Rlight
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(0)
        self.drive.moveDist(300, heading=0)
        self.drive.moveArc(-260, -70, speed=150)
        self.drive.moveDist(430, heading=-70)
        self.drive.moveDist(50, heading=-78, turn=False)
        self.runArmAngle(-500, 580)
        self.runArmAngle(500, 580)
        self.drive.moveDist(-90)
        self.drive.moveArc(-140, 180)

        # self.drive.turnTo(-69)
        # self.drive.moveDist(620, heading=-69)
        # self.drive.moveRGB(self.Llight, [54, 85, 79], tolerance=10)
        # self.drive.moveDist(50, heading=-72)
        # self.drive.turnTo(-90, speed=70)
        # self.drive.moveDist(130, heading=-90, turn=False)
        # self.drive.drive.drive(0, 40)
        # self.wait(500)
        # self.drive.stop()
        # Thread(target=self.runArmAngle, args=[-500, 580]).start()
        # self.wait(2000)
        # self.drive.moveDist(-140, turn=False)
        # Thread(target=self.runArmAngle, args=[1000, 620]).start()
        # self.drive.moveArc(-140, 180)
        # Thread(target=self.runArmAngle, args=[-400, 530]).start()
        # self.drive.moveDist(-180, heading=180, speed=100)
        # self.drive.moveDist(210, heading=180, speed=100)
        # self.runArmAngle(200, 200)
        

        # self.drive.moveDist(520, heading=0)
        # self.drive.turnTo(-68)
        # self.drive.moveDist(440, heading=-68)
        # self.drive.moveRGB(self.Llight, [57, 85, 79])
        # self.drive.moveDist(100, heading=-75)
        # self.drive.turnTo(-85, speed=70)
        # self.runArmAngle(-500, 600)
        # self.drive.moveDist(-100, heading=-90, turn=False)
        # Thread(target=self.runArmAngle, args=[1000, 600]).start()
        # self.drive.moveArc(-150, 180)
        # Thread(target=self.runArmAngle, args=[-1000, 530]).start()
        # self.drive.moveDist(-150, heading=180, speed=100)
        # self.drive.moveDist(180, heading=180)
        # self.runArmAngle(200, 210)


        # self.drive.moveDist(200, heading=-90)
        # self.drive.moveLight(self.Rlight, [0, 15])
        # self.drive.moveDist(400, heading=-77, turn=False)
        # self.drive.moveLight(self.Rlight, [0, 10])
        # self.drive.moveDist(110, heading=-77, turn=False)
        # self.drive.turnTo(0)
        # self.runArmAngle(-300, 450)
        # self.drive.moveDist(-50, heading=0, turn=False)
        # self.drive.moveLight(self.Llight, [0, 5])
        # # self.drive.moveDist(60, heading=0)
        # self.runArmAngle(1000, 165)
        # self.wait(1000)
        # self.drive.moveDist(-70, heading=0)
        # Thread(target=self.runArmAngle, args=[1000, 160]).start()
        # self.drive.turnTo(-45)
        # self.drive.moveDist(250, heading=-45)
        # self.drive.turnTo(0)
        # self.drive.moveDist(410, heading=0)

        self.config.state.setState(1)

    def runArmAngle(self, speed, angle):
        self.config.LMmotor.run_angle(speed, angle, wait=False)
        self.config.RMmotor.run_angle(-speed, angle, wait=True)
    
    def runArmTime(self, speed, time):
        self.config.LMmotor.run_time(speed, time, wait=False)
        self.config.RMmotor.run_time(-speed, time)