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
        self.drive.moveDist(190, heading=0)
        self.drive.moveArc(-400, -80, speed=200)
        self.drive.moveArc(150, -65, speed=200)
        self.drive.moveDist(190, heading=-65)
        self.drive.turnTo(-90)
        self.drive.moveDist(90, heading=-90, turn=False)
        Thread(target=self.turnIntoPurple).start()
        Thread(target=self.runArmAngle, args=[-500, 540]).start()
        self.wait(1500)
        self.drive.moveDist(-102, heading=-90, turn=False)
        Thread(target=self.runArmAngle, args=[600, 580]).start()
        self.drive.moveArc(-132, 180, speed=150, timeout=4000)

        Thread(target=self.runArmAngle, args=[-400, 530]).start()
        self.drive.moveDist(-180, turn=False)
        self.drive.moveDist(210, turn=False)
        self.runArmAngle(200, 220)

        self.config.state.setState(1)

    def runArmAngle(self, speed, angle):
        self.config.LMmotor.run_angle(speed, angle, wait=False)
        self.config.RMmotor.run_angle(-speed, angle, wait=True)
    
    def runArmTime(self, speed, time):
        self.config.LMmotor.run_time(speed, time, wait=False)
        self.config.RMmotor.run_time(-speed, time)
    
    def turnIntoPurple(self):
        self.drive.drive.drive(0, 50)
        self.wait(2000)
        self.drive.stop()