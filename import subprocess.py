import subprocess
import sys
import time
from statistics import mean

def ping_host(host, count=4):
    """
    Ping a host and return the results
    """
    try:
        if sys.platform == 'win32':
            cmd = ['ping', '-n', str(count), host]
        else:
            cmd = ['ping', '-c', str(count), host]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"
// 解析ping输出，提取ping时间
def parse_ping_times(output):
    """
    Extract ping times from ping output
    """
    times = []
    lines = output.split('\n')
    
    for line in lines:
        if 'time=' in line:
            try:
                time_str = line.split('time=')[1].split('ms')[0].strip()
                times.append(float(time_str))
            except:
                pass
    
    return times

def main():
    print("=" * 50)
    print("Network Speed Ping Tool")
    print("=" * 50)
    
    # Test multiple hosts
    hosts = [
        "8.8.8.8",      # Google DNS
        "1.1.1.1",      # Cloudflare DNS
        "8.8.4.4"       # Google DNS alternate
    ]
    
    all_times = []
    
    for host in hosts:
        print(f"\nPinging {host}...")
        output = ping_host(host, count=4)
        print(output)
        
        times = parse_ping_times(output)
        all_times.extend(times)
    
    if all_times:
        print("\n" + "=" * 50)
        print("Summary Statistics:")
        print("=" * 50)
        print(f"Min Ping: {min(all_times):.2f}ms")
        print(f"Max Ping: {max(all_times):.2f}ms")
        print(f"Avg Ping: {mean(all_times):.2f}ms")
        print("=" * 50)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()