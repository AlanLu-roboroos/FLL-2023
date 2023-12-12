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
        self.drive.moveDist(180, heading=-35)
        self.drive.moveLight(self.Llight, [0, 10])
        self.drive.turnTo(-38)
        self.drive.moveDist(135, heading=-38)
        self.drive.turnTo(45)
        self.drive.moveDist(140, heading=45)
        self.arm.run_angle(600, 300)
        Thread(target=self.returnArm).start()
        self.drive.setHead(47)
        self.drive.moveDist(-220, heading=45)
        self.drive.turnTo(110)
        self.drive.moveDist(-450, heading=110)
        self.arm.run_angle(-400, 230)
        self.drive.turnTo(180)
        # self.drive.moveDist(85, heading=180)
        self.drive.moveArc(-110, 90, speed=100)
        # Thread(target=self.raiseArmAfterFlower).start()
        self.drive.moveDist(420, turn=False, heading=90)
        self.drive.spinTo(160)
        self.drive.moveDist(600, heading=160, down=False)

        self.config.state.setState(1)
    
    def returnArm(self):
        self.wait(200)
        self.arm.run_angle(-400, 100)
        self.wait(2000)
        self.arm.run_angle(400, 100)
    
    def raiseArmAfterFlower(self):
        self.arm.run_angle(400, 200)
