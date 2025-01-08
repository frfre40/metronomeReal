from clicktrack import *

intro = Measure(120, '3/4') + Measure(120, '4/4') * 7
chorus = Measure(120, '3/4') * 8
verse = Measure(120, '4/4') * 16
bridge = Measure(140, '6/8') * 8

song = intro + verse + chorus + verse + chorus + bridge + chorus*2 + Measure(120, '1/4')
song = chorus + bridge

# song.play()

test = Measure(146, '5/4', '31121') * 12
test.play()
