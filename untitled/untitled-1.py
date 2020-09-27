#coding: utf-8
import cocos
def Repeat(self):
    cocos.actions.Repeat(self)
cocos.director.director.init(width = 600, height = 600)
root = cocos.scene.Scene()
t = cocos.text.Label("Hello world!", position = (100, 200))
root.add(t)
t.do(Repeat(cocos.actions.RotateBy(360, 3)))
cocos.director.director.run(root)

