#coding=utf-8


def taxi_process(ident, trips, start_time=0):   # 1
    """每次改变状态时创建事件,把控制权让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage')   # 2
    for i in range(trips):  # 3
        time = yield Event(time, ident, 'pick up passenger')    # 4
        time = yield Event(time, ident, 'drop off passenger')   # 5
    yield Event(time, ident, 'going home')  # 6
    # 出租车进程结束   # 7


class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):    # 1
        """排定并显示事件,直到时间结束"""
        # 排定各辆出租车的第一个事件
        for _, proc in sorted(self.procs.items()):  # 2
            first_event = next(proc)    # 3
            self.events.put(first_event)    # 4
        # 这个仿真系统的主循环
        sim_time = 0    # 5
        while sim_time < end_time:  # 6
            if self.events.empty():     # 7
                print('*** end of events ***')
                break
            current_event = self.events.get()   # 8
            sim_time, proc_id, previous_action = current_event  # 9
            print('taxi:', proc_id, proc_id * ' ', current_event)   # 10
            active_proc = self.procs[proc_id]   # 11
            next_time = sim_time + compute_duration(previous_action)    # 12
            try:
                next_event = active_proc.send(next_time)    # 13
            except StopIteration:
                del self.procs[proc_id]     # 14
            else:
                self.events.put(next_event)     # 15
        else:   # 16
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


if __name__ == '__main__':
    taxi = taxi_process(ident=13, trips=2, start_time=0)    # 1
    next(taxi)  # 2
    taxi.send(_.time + 7)   # 3
    taxi.send(_.time + 23)  # 5
    taxi.send(_.time + 5)   # 6
    taxi.send(_.time + 48)  # 7
    taxi.send(_.time + 10)  # 9