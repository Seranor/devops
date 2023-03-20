import psutil
if __name__ == '__main__':
    """查看cpu个数"""
    # print( psutil.cpu_count() )  # 4，逻辑CPU个数
    # print( psutil.cpu_count(logical=False) ) # 2，物理CPU个数

    # print( psutil.cpu_times(percpu=True) )
    # scputimes(
    #   user=937.05,    # 用户进程使用的CPU时间累计
    #   nice=26.94,     # 优先级为负值的进程使用时间
    #   system=211.48,  # 系统内核进程使用时间累计
    #   idle=1480.49,   # CPU空闲时间累计
    #   iowait=15.02,   # 等待IO花费的时间
    #   irq=0.0,        # 硬中断时间累计
    #   softirq=26.94,  # 软中断时间累计
    #   steal=0.0,      # 花费在虚拟机中的时间
    #   guest=0.0,
    #   guest_nice=0.0
    # )

    """查看cpu运行状态比例信息"""
    # print(psutil.cpu_times_percent())
    # scputimes(user=0.0, nice=0.0, system=0.0, idle=1.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)

    """查看cpu利用率"""
    # print( psutil.cpu_percent(interval=None) )  # 0.0
    # print( psutil.cpu_percent(interval=1) )  # 4.3
    # print( psutil.cpu_percent(percpu=True) )  # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    """CPU的统计信息"""
    # print(psutil.cpu_stats())
    # scpustats(
    #   ctx_switches=6672143,  # 自操作系统启动的上下文切换次数
    #   interrupts=4119465,    # 自操作系统启动以来的中断数
    #   soft_interrupts=2539436,  # 自操作系统启动以来的软中断数
    #   syscalls=0                # 自操作系统启动以来的系统调用次数
    # )

    """CPU的频率"""
    # print(psutil.cpu_freq())
    # scpufreq(
    #   current=2208.0,   # 当前频率
    #   min=0.0,          # 最小频率
    #   max=0.0           # 最大频率
    # )

    """以元组的形式返回最近1、5和15分钟内的平均系统负载。"""
    # print(psutil.getloadavg())  # (0.48, 0.39, 0.22)

    """获取内存信息"""
    # print(psutil.virtual_memory())
    # svmem(
    #   total=5420404736,     # 总物理内存，total = used + free
    #   available=1328689152, # 可用内存，free = buffers + cached
    #   percent=75.5,         # 已用内存的百分比，percent=(total - available) / total * 100
    #   used=3783630848,      # 物理已使用的内存
    #   free=112947200,       # 物理没使用的空闲内存
    #   active=818221056,     # 当前正在使用或最近使用的内存
    #   inactive=3860795392,  # 未使用的内存
    #   buffers=98254848,     # 缓冲区内存
    #   cached=1425571840,    # 缓存占用内存
    #   shared=8818688,       # 可以被多个进程同时访问的内存
    #   slab=289615872        # 缓存内核数据结构的内存
    # )

    """以人类可读的方式输出内存大小"""
    # from psutil._common import bytes2human
    # ret = bytes2human(psutil.virtual_memory()[0])
    # print(ret)  # 5.0G

    """系统交换内存统计信息"""
    # print(psutil.swap_memory())
    # sswap(
    #   total=2147479552,   # 总交换内存
    #   used=284708864,     # 已使用的交换内存
    #   free=1862770688,    # 未使用过的空闲交换内存
    #   percent=13.3,       # 已用交换内存的百分比，percent=(total - available) / total * 100
    #   sin=100696064,      # 系统累积从硬盘转入的字节数
    #   sout=342335488      # 系统累积从硬盘转出的字节数
    # )

    """磁盘分区数据"""
    # print(psutil.disk_partitions())
    # [
    #   sdiskpart(device='设备路径', mountpoint='挂载点路径', fstype='分区文件系统', opts='以逗号分隔的字符串，指示驱动器/分区的不同挂载选项'),
    #   sdiskpart(device='/dev/sda5', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro'),
    #   sdiskpart(device='/dev/loop0', mountpoint='/snap/core18/2284', fstype='squashfs', opts='ro,nodev,relatime'),
    #   sdiskpart(device='/dev/sda1', mountpoint='/boot/efi', fstype='vfat', opts='rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro')
    # ]

    """获取指定路径所属的分区磁盘的使用统计信息"""
    # print(psutil.disk_usage("/"))
    # sdiskusage(
    #   total=52044496896,  # 总磁盘空间
    #   used=40965885952,   # 已用磁盘空间
    #   free=8404480000,    # 用户可用的空间
    #   percent=83.0        # 用户对磁盘的利用率
    # )

    """磁盘io操作相关信息"""
    # print(psutil.disk_io_counters())
    # sdiskio(
    #   read_count=130506,  # 读取次数
    #   write_count=74714,  # 写入次数
    #   read_bytes=4225399296,  # 读取的字节数
    #   write_bytes=3102049280, # 写入的字节数
    #   read_time=52547,        # 从磁盘读取所花费的时间（以毫秒为单位）
    #   write_time=24460,       # 写入磁盘所花费的时间（以毫秒为单位）
    #   read_merged_count=48032,   # 合并读取的数量
    #   write_merged_count=152722, # 合并写入的数量
    #   busy_time=178944        # 实际 I/O 所花费的时间 (以毫秒为单位)
    # )

    """获取网络 I/O 统计信息"""
    # print(psutil.net_io_counters())
    # snetio(
    #   bytes_sent=1416706,   # 网卡接收的数据字节数
    #   bytes_recv=14261510,  # 网卡接收的数据字节数
    #   packets_sent=20303,   # 网卡发送的数据包数
    #   packets_recv=27037,   # 网卡接收到的数据包数
    #   errin=0,              # 网卡接收数据时的错误总数
    #   errout=0,             # 网卡发送数据时的错误总数
    #   dropin=0,             # 网卡在网络请求被丢弃的传入数据包总数
    #   dropout=0             # 网卡在网络请求被丢弃的传出数据包总数
    # )

    # print(psutil.net_io_counters().bytes_sent)
    # print(psutil.net_io_counters().bytes_recv)
    # print(psutil.net_io_counters().packets_sent)
    # print(psutil.net_io_counters().packets_recv)

    """网卡的连接信息"""
    # print(psutil.net_connections())
    # [
    #   sconn(fd=套接字文件描述符(windows和Linux下为-1), family=地址族, type=地址类型, laddr=本地地址, raddr=绝对地址, status=TCP连接的状态, pid=打开套接字的进程的 PID进程ID),
    #   sconn(fd=-1, family=<AddressFamily.AF_INET6: 10>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='::', port=22), raddr=(), status='LISTEN', pid=None),
    #   sconn(fd=-1, family=<AddressFamily.AF_INET6: 10>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='::', port=22), raddr=(), status='LISTEN', pid=None),
    #   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=22), raddr=(), status='LISTEN', pid=None),
    #   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=6379), raddr=(), status='LISTEN', pid=None),
    #   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='192.168.233.129', port=68), raddr=addr(ip='192.168.233.254', port=67), status='NONE', pid=None),
    #   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=80), raddr=(), status='LISTEN', pid=None),
    #   sconn(fd=67, family=<AddressFamily.AF_INET6: 10>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='::ffff:127.0.0.1', port=63342), raddr=(), status='LISTEN', pid=3993),
    # ]

    """网卡的地址信息"""
    # print(psutil.net_if_addrs())
    # {
    #   'lo': [
    #     snicaddr(family=地址族, address='主网卡地址', netmask='网络掩码地址', broadcast=广播地址, ptp=点对点接口（通常是 VPN）上的目标地址),
    #     snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None),
    #     snicaddr(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
    #     snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)
    #   ],
    #   'ens33': [
    #     snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.233.129', netmask='255.255.255.0', broadcast='192.168.233.255', ptp=None),
    #     snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::59eb:3d0b:84e:950f%ens33', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
    #     snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:0c:29:7e:42:9d', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)
    #   ]
    # }

    """网卡的状态信息"""
    # print(psutil.net_if_stats())
    # # {
    # #   'lo': snicstats(isup=表示以太网电缆或 Wi-Fi 已连接, duplex=双工通信类型, speed=网卡速度, mtu=网卡的最大传输单位，以字节表示),
    # #   'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536),
    # #   'ens33': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1000, mtu=1500)
    # # }

    """系统启动时间"""
    # print(psutil.boot_time())  # 1650281599.0

    """当前连接到操作系统的用户列表"""
    # print(psutil.users())
    # [
    #   用户类型(name='用户账号名', terminal='终端类型', host='客户端地址', started=创建连接的时间戳, pid=进程ID)
    #   suser(name='moluo', terminal=':0', host='localhost', started=1650267136.0, pid=2837)
    # ]
