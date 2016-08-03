Blueprint module:
  Base support for visual coding tool.

Install:
  python setup.py sdist
   python setup.py install
   
Usage:
    Blueprint.Bp_debug = True
    security_filter_task = SetSecurityPoolTask("filterSecuiry")
    order_task = SetOrderTask("OrderTask")

    selector = Selector("Selector")
    selector.AddTask(security_filter_task)

    sequencer = Sequence("Sequencer")
    sequencer.AddTask(security_filter_task)
    sequencer.AddTask(order_task)

    sequencer.AddTask(selector,11)
    sequencer.SwapTask(0,2)
    sequencer.Evolution()