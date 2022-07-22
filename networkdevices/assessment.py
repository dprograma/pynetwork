"""
This program uses Python socket module for bidirectional commnuncation channel between differenct machines. It provides solutions to the following requirements.

1. Ping a single host
    a. By IP
    b. By name
2. Ping multiple hosts
3. Port Scan
4. Trace Route

The program creates a DeviceNetwork class with the following methods.

1. ping_host_by_ip
2. ping_host_by_name
3. ping_multiple_hosts
4. port_scan
5. create_receiver
6. create_sender
7. route_tracer


Note:
The program will require root (administrative) privileges at some point (when using RAW socket type), so a terminal with admin privileges should be used to run the program.

"""
import subprocess
import platform
import socket  
import time


class DeviceNetwork:
    start_time = time.time()
    # create the class constructor

    def __init__(self):
        self.start_time = DeviceNetwork.start_time

    # create the ping host by ip function
    def ping_host_by_ip(self, ip):
        """
        Pseudocode:
            Retrieve the IP value supplied by the user through the terminal.
            Write an if statement to determine the if the type of IP supplied is a list or a string.
            If the type of IP supplied is a list, perform a for loop on each item in the list.
            If the operating system is 'windows', use parameter '-n' in the ping command otherwise use '-c'.
            Ping each IP and retrieve a response. 
            If the response is 0 then print 'IP is up' else print 'IP is down' to the console.
        
        Args:
            ip (string or list of strings): contains an IP or a list of IPs to initiate a ping program

        Returns:
            Return a response 0 if IP ping is True
        """
        if type(ip) is list:  # to ping a list of IPs
            for i in ip:
                params = '-n' if platform.system().lower() == 'windows' else '-c'
                # Building the command. Ex: "ping -c 1 google.com"
                command = ['ping', params, '1', str(i)]
                response = subprocess.call(command)
                if response == 0:
                    print(f'{i} is up.')
                else:
                    print(f'{i} is down.')
                print(f"Time taken: {time.time() - self.start_time:.2f}s")
                return response
        else:  # to ping a single IP
            params = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', params, '1', str(ip)]
            response = subprocess.call(command)
            if response == 0:
                print(f'{ip} is up.')
            else:
                print(f'{ip} is down.')
            print(f"Time taken: {time.time() - self.start_time:.2f}s")
            return response

    # create the ping host by name function
    def ping_host_by_name(self):
        """
        Pseudocode:
            Start a try/except exception handler to handle socket error.
            Retrieve hostname value supplied by the user through the console.
            Get the IP value of the supplied hostname.
            call the ping_host_by_ip function to ping the IP returned.
            If there is an exception, print 'Cannot resolve host name' to the console.
            call ping_host_by_name function recursively.
        """
        try:
            target = input("Enter the host name: ")
            ip = socket.gethostbyname(target)
            # call ping_host_by_ip function to ping the IP
            self.ping_host_by_ip(ip)
        except socket.gaierror:
            print(f"Cannot resolve host name {target}")
            self.ping_host_by_name()

    # create the ping multiple hosts function

    def ping_multiple_hosts(self, ips):
        """
        Pseudocode:
            Supply comma separated IPs/hostnames in the console.
            Split the comman seperated IPs/hostnames into a list of IP/hostname items called 'ip_list'.
            Create an empty list to store items; name it 'ip_addr'.
            Perform a for loop on each item in ip_list to do the following:
                Start a try/except exception handler to print 'Cannot resolve IP' at the console if it encounters an error.
                Print 'Resolving IP' to the console. 
                get the IP of each hostname and store them as list items in ip_addr.
            Perform another for loop on each item in ip_addr list.
            call the ping_host_by_ip function and pass the ip_addr list to it as a parameter.           

        Args:
            ips (list): A list of host names supplied by user.
        """
        ip_list = ips.split(",")

        ip_addr = []  # create an empty array to store the newly created IPs

        for i in range(len(ip_list)):
            try:
                print("Resolving: ", ip_list[i])
                ip_addr.append(str(socket.gethostbyname(ip_list[i].strip())))
            except:
                print("Cannot resolve: ", ip_list[i])
        for i in range(len(ip_addr)):
            print(f"{ip_list[i]} - {ip_addr[i]}")

        self.ping_host_by_ip(ip_addr)

    # create the port scan function
    def port_scan(self, ips, rn1, rn2):
        """
        Pseudocode:
            Store initial value of socket connection value in a 'connect' as 1 (True).
            Create an empty list 'ip_list' to store list of IPs supplied by user.
            Create a try/except exception handler to handle Attrubute, Socket, Type, Value errors.
            Retrieve comma separated hostnames supplied by user through the console.
            Split the comma separated hostname and store them as items in ip_list.
            Retrieve first and second port range values and convert them to integer values.
            Perform a for loop on each item in ip_list to do the following:
            Get the IP value from the hostnames in ip_list.
            Print 'Target IP'.
            Print 'Starting scan on host'.
            Start a try/except exception handler to handle socket error.
            Perform another for loop on each item in the port range ex. 80 - 443 and do the follwing:
            Create a socket connection.
            Scan the IP against the port and retrieve a response.
            If the response is 0 (True) then print 'Connection established on port number'.
            Close the connection.
            If the response is otherwise, close the connection.
            Return the connection value.
                
        Args:
            ips (list): List of IPs to be scanned
            rn1 (int): first range value for the port to be scanned
            rn2 (int): second range value for the port to be scanned
        Returns:
            Returns 0 if the connection is True
        """
        connect = 1
        ip_list = []
            
        try:
            ip_list = ips.split(",")
            rn1 = int(rn1)
            rn2 = int(rn2)
            for i in range(len(ip_list)):
                target_IP = str(socket.gethostbyname(ip_list[i].strip()))
                print("Target IP", target_IP)
                print(f"Starting scan on host {target_IP} ({ip_list[i]})")

                try:
                    for r in range(rn1, rn2):
                            self.server = socket.socket(
                                socket.AF_INET, socket.SOCK_STREAM)
                            connect = self.server.connect_ex((target_IP, r))
                            if connect == 0:
                                print("Connection established on port ", r)
                                print(
                                    f"Time taken: {time.time() - self.start_time:.2f}s")
                                self.server.close()
                            else:
                                self.server.close()
                except socket.gaierror:
                    print("Problem while scanning port ", r)
        except AttributeError:
            print(
                "Invalid Entry. Paste the IPs/hostnames separated commas ex. yahoo.com, google.com") 
        except socket.gaierror:
                    print(f"Invalid host name {ip_list[i]} provided.")
        except TypeError:
            print("Invalid port numbers ", rn1, rn2, sep=", ")
        except ValueError:
            print("Invalid port numbers ", rn1, rn2, sep=", ")
                    
        return connect
    
    # create the receiver (server) function

    def create_receiver(self, port):
        """
        Pseudocode:
            Create a variable 's' with an initial value of None.
            Create a try/except exception handler to handle Socket, OSError, Type and Value errors.
            Retrieve port value supplied by the user through the console and convert it to an integer if not already one.
            Create a RAW socket connection instance and assign it to the initial variable 's'.
            Allow incoming IP connections to the port supplied.
            Return the socket connection instance 's'.            

        Args:
            port (int): Destination host port

        Raises:
            IOError: Socket error (if any)

        Returns:
            A socket instance
        """
        s = None
        
        try:
            port = int(port)
            s = socket.socket(family=socket.AF_INET,
                          type=socket.SOCK_RAW)
            s.bind(('', port))  # allows any incoming socket connection
            print("Listening for incoming connection...")
        except socket.error as e:
            raise IOError(f"Unable to bind receiver socket: {e}")
        except OSError:
            print(f"Unable to resolve port value.")
        except TypeError:
            print(f"Unable to resolve port value")
        except ValueError:
            print(f"Unable to resolve port value")
        return s 

    # create the sender (client) function
    def create_sender(self, ttl):
        """
        Pseudocode:
            Create a variable 's' with an initial value of None.
            Create a try/except exception handler to handle Socket, OSError, Type and Value errors.
            Retrieve time-to-live value supplied by the user through the console and convert it to an integer if not already one.
            Create a UDP socket connection instance and assign it to the initial variable 's'.
            Set the socket connection options.
            Return the socket connection instance 's'.  

        Args:
            ttl (int): time-to-live value

        Returns:
            A socket instance
        """
        s = None
        try:
            ttl = int(ttl)
            s = socket.socket(family=socket.AF_INET,
                            type=socket.SOCK_DGRAM)

            s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            print("Connection created with server...")
        except socket.error as e:
            raise IOError(f"Unable to bind receiver socket: {e}")
        except OSError:
            print(f"Unable to resolve port value.") 
        except TypeError:
            print(f"Unable to resolve port value")
        except ValueError:
            print(f"Unable to resolve port value")

        return s

    # route tracer function
    def route_tracer(self, ip, port, hops=30):
        """
        Pseudocode:
            Set the initial time-to-live (ttl) for a connection to 1.
            Set the initial target IP value nameed 'target_IP' to trace to None.
            Set the initial connected IP value to a tuple with a single empty string value.
            Create a try/except exception handler to handle Socket, OSError and Type errors.
            Get the IP of the user supplied hostname and assign it to the target_IP value.
            Print 'Trace route to hostname, ip, and number of hops'.
            Perform a while loop to do the following:
            Call the create_receiver function entering the user supplied port value as a parameter and retrieve the RAW socket connection instance.
            Call the create_sendeer function entering the user supplied time-to-live value as a parameter and retrieve the UDP socket connection instance.
            Send a request to the create_receiver instance with the target_IP and port value.
            Create a try/except/finally exception handler to handle IOError error and finally close the create_receiver and create_sender socket instances.
            Retrieve a response from the create_receiver instance.
            If the response is a tuple with the connected IP as tuple single value, then print the ttl and IP.
            return the connected IP. 

        Args:
            ip (string): Destination host to be probed 
            port (int): host port 
            hops (int, optional): Maximum number of hops to probe. Defaults to 30.

        Raises:
            IOError: Socket error
            
        Return:
            Returns connected client IP address
        """
        ttl = 1
        target_IP = None
        addr = ('',)
        
        try:
            target_IP = socket.gethostbyname(str(ip))
            print(f"Traceroute to {ip} ({target_IP}), {hops} hops max.")

        # while the time-to-live increments by 1 we loop through until the it is equal to the given number of hops we require i.e 30 hops
            while True:
                # call the receiver socket instance
                receiver = self.create_receiver(int(port))
                # call the sender socket instance
                sender = self.create_sender(ttl)
                # send a request to the receiver instance
                sender.sendto(b'', (target_IP, int(port)))

                try:
                    # response from the receiver
                    data, addr = receiver.recvfrom(1024)
                except socket.error as e:
                    raise IOError(f"Socket error {e}")
                finally:
                    # close the socket instances
                    receiver.close()
                    sender.close()

                # if IP address is tracable, print the address
                if addr:
                    print(f"{ttl:<4} {addr[0]}")
                else:
                    print(f"{ttl:<4} *")

                ttl += 1  # increment ttl

                # stop the program if the number of loops exceeds the total number of hops i.e 30 hops
                if addr[0] == ip or ttl > hops:
                    break
        except socket.gaierror:
            print(f"Cannot resolve {ip}")
        except socket.error as e:
            raise IOError(f"Unable to resolve {ip}: {e}")
        except OSError:
            print(f"Cannot resolve hostname {ip}")
        except TypeError:
            print()
        return addr[0]

# main program area
if __name__ == "__main__":
    request = DeviceNetwork()

    while True:
        print("Enter 'i' to ping device by IP.")
        print("Enter 'n' to ping device by name.")
        print("Enter 'm' to ping multiple devices.")
        print("Enter 's' for port scan.")
        print("Enter 't' to perform a traceroute.")
        print("Enter 'q' to quit the program.")
        r = input(">>>? ")
        if r == "i":
            ip = input("Enter the host ip address: ")
            request.ping_host_by_ip(ip)
            q = input("Do you want to continue? (Y/N) ").lower()
            if q == "y":
                pass
            elif q == "n":
                break

        elif r == "n":
            request.ping_host_by_name()
            q = input("Do you want to continue? (Y/N) ").lower()
            if q == "y":
                pass
            elif q == "n":
                break
        elif r == "m":
            list_ips = input(
                "Type or paste the comma separated ips/hostname here: \n")
            request.ping_multiple_hosts(list_ips)
            q = input("Do you want to continue? (Y/N) ").lower()
            if q == "y":
                pass
            elif q == "n":
                break
        elif r == "s":
            list_ips = input(
                "Type or paste the comma separated ips/hostnames here: \n")
            r1 = input("Enter the first value of the range: \n")
            r2 = input("Enter the second value of the range: \n")
            request.port_scan(list_ips, r1, r2)
            q = input("Do you want to continue? (Y/N) ").lower()
            if q == "y":
                pass
            elif q == "n":
                break
        elif r == "t":
            list_ips = input(
                "Type or paste the ip/hostname here: \n")
            ip_port = input("Enter the port number to trace. \n")
            request.route_tracer(list_ips, ip_port)
            q = input("Do you want to continue? (Y/N) ").lower()
            if q == "y":
                pass
            elif q == "n":
                break
        elif r == "q":
            break
        else:
            print("Invalid entry. Please, follow the instruction below.")
            print()
            pass
