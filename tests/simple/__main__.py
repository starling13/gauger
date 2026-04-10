import gauge
import gauge.round_gauge
import gauge.exporter

gauge1 = gauge.round_gauge.Object()

scale1 = gauge.scale.Object()
gauge1.add_scale(scale_object=scale1)
scale1.range = (0.0, 10.0)
scale1.maj_ticks.count = 10

mt1 = gauge.Ticks()
scale1.add_minor_ticks(ticks=mt1)
mt1.count = 1

exporter = gauge.exporter.Object()
exporter.export(obj=gauge1, file_path="test_py.svg")
