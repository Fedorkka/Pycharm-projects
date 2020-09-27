#coding: utf-8
import cocos

class RotatingText(cocos.text.Label):
    # инициализируем базовый класс и настраиваем обратный вызов
    def __init__(self, text = "", position = (0, 0)):
        super(RotatingText, self).__init__(text, position)
        self.schedule(self.update)

    # функция обратного вызова, модифицируем угол поворота в зависимости от прошедшего времени
    def update(self, dt):
        self.rotation += dt * 20

cocos.director.director.init()
scene = cocos.scene.Scene()
scene.add(RotatingText("Hello world!", (100, 200)))
cocos.director.director.run(scene)