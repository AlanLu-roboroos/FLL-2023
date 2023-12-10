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

        self.drive.moveDist(320, heading=0)
        self.drive.turnTo(-35)
        self.drive.moveDist(200, heading=-35)
        self.drive.moveLight(self.Rlight, [0, 10])
        self.drive.moveDist(125, heading=-35)
        self.drive.turnTo(45)
        self.drive.moveDist(180, heading=45)
        self.arm.run_angle(400, 200)
        Thread(target=self.returnArm).start()
        self.drive.setHead(47)
        self.drive.moveDist(-200, heading=45)

        self.config.state.setState(1)
    
    def returnArm(self):
        self.wait(200)
        self.arm.run_angle(-400, 100)
