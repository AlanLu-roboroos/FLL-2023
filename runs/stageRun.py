from threading import Thread


class StageRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.Llight = config.Llight
        self.Rlight = config.Rlight
        self.arm = config.LMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(0)

        self.drive.moveDist(300, heading=0)
        self.drive.turnTo(-32)
        # self.drive.moveDist(260, heading=-33)
        self.drive.moveDist(425, heading=-35, turn=False)
        self.drive.turnTo(45)
        self.drive.moveDist(140, heading=45)
        self.arm.run_angle(600, 300)
        Thread(target=self.returnArm).start()
        self.drive.setHead(47)
        self.drive.moveDist(-210, heading=45)
        self.drive.turnTo(110)
        self.drive.moveDist(-450, heading=110)
        self.arm.run_angle(-400, 230)
        self.drive.turnTo(180)
        # self.drive.moveDist(85, heading=180)
        self.drive.moveArc(-110, 90, speed=150)
        # Thread(target=self.raiseArmAfterFlower).start()
        self.drive.moveDist(320, turn=False, heading=90)
        self.drive.moveArc(400, 160, speed=400)
        self.drive.moveDist(400, heading=160, down=False, up=False)

        self.config.state.setState(1)
    
    def returnArm(self):
        self.wait(200)
        self.arm.run_angle(-400, 100)
        self.wait(2000)
        self.arm.run_angle(400, 100)
    
    def raiseArmAfterFlower(self):
        self.arm.run_angle(400, 200)
