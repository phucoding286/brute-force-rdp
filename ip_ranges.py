global_list_ip = []
start_ip_units = None
end_ip_units = None

def ip_range(start: str, end: str):
    global global_list_ip
    global start_ip_units
    global end_ip_units
    
    if start_ip_units is None and end_ip_units is None:
        start_ip_units = [int(n_ip) for n_ip in start.split(".")]
        end_ip_units = [int(n_ip) for n_ip in end.split(".")]

    if start_ip_units[0] == end_ip_units[0] and start_ip_units[1] == end_ip_units[1] \
        and start_ip_units[2] == end_ip_units[2] and start_ip_units[3] == end_ip_units[3]:
        return "end"

    if start_ip_units[3]-1 == 255:
        start_ip_units[2] += 1
        start_ip_units[3] = 0

    elif start_ip_units[2]-1 == 255:
        start_ip_units[1] += 1
        start_ip_units[2] = 0
    
    elif start_ip_units[1]-1 == 255:
        start_ip_units[0] += 1
        start_ip_units[1] = 0
    
    else:
        start_ip_units[3] += 1
        global_list_ip.append(".".join([str(ip) for ip in start_ip_units]))

def mul_t_ip_range(start, end):
    while True:
        t_ip_r = ip_range(start, end)
        if t_ip_r == "end":
            break

start = input("nhập ip bắt đầu: ")
end = input("nhập ip kết thúc: ")
o_f = input("nhập đường dẫn file đầu ra hoặc bỏ trống (để mặc định): ")

if o_f == "":
    o_f = "targets.txt"

mul_t_ip_range(start, end)
      
with open(o_f, "a", encoding="utf-8") as f:
    for ip in global_list_ip:
        f.write(ip+"\n")