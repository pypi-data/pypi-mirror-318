import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from .utils import Logger

class Scanner:
    def __init__(self, timeout=1):
        self.timeout = timeout
        self.logger = Logger()

    def scan_network(self, network):
        """Scannt ein Netzwerk nach aktiven Hosts"""
        try:
            network = ipaddress.ip_network(network)
            results = {}
            
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = [executor.submit(self._scan_host, str(ip)) 
                          for ip in network.hosts()]
                
                for future in futures:
                    ip, data = future.result()
                    if data:
                        results[ip] = data
            
            return results
        except Exception as e:
            self.logger.error(f"Netzwerk-Scan fehlgeschlagen: {e}")
            return {}

    def port_scan(self, host, ports=None):
        """Scannt spezifische Ports eines Hosts"""
        if ports is None:
            ports = range(1, 1025)
        
        open_ports = {}
        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(self.timeout)
                    result = s.connect_ex((host, port))
                    if result == 0:
                        service = self._get_service_name(port)
                        open_ports[port] = service
            except:
                continue
        return open_ports

    def vulnerability_scan(self, host):
        """Führt einen grundlegenden Vulnerability Scan durch"""
        vulnerabilities = []
        basic_checks = [
            self._check_default_credentials,
            self._check_open_ports,
            self._check_ssl_cert
        ]
        
        for check in basic_checks:
            result = check(host)
            if result:
                vulnerabilities.append(result)
        
        return vulnerabilities

    def _scan_host(self, ip):
        """Scannt einen einzelnen Host"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                hostname = socket.gethostbyaddr(ip)[0]
                open_ports = self.port_scan(ip)
                return ip, {
                    'hostname': hostname,
                    'open_ports': open_ports,
                    'status': 'active'
                }
        except:
            return ip, None

    def _get_service_name(self, port):
        """Ermittelt den Service-Namen für einen Port"""
        try:
            return socket.getservbyport(port)
        except:
            return "unknown"

    def show_results(self, results):
        """Zeigt die Scan-Ergebnisse an"""
        for ip, data in results.items():
            print(f"\nHost: {ip}")
            if data:
                print(f"Hostname: {data['hostname']}")
                print("Offene Ports:")
                for port, service in data['open_ports'].items():
                    print(f"  {port}/tcp\t{service}")
            else:
                print("Host nicht erreichbar") 

    def service_detection(self, host, port):
        """Detaillierte Service-Erkennung"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                s.connect((host, port))
                
                # Banner Grabbing
                banner = s.recv(1024).decode('utf-8', errors='ignore')
                
                service_info = {
                    'port': port,
                    'service': self._get_service_name(port),
                    'banner': banner if banner else 'No banner',
                    'version': self._extract_version(banner)
                }
                
                return service_info
        except Exception as e:
            self.logger.error(f"Service-Erkennung fehlgeschlagen: {e}")
            return None

    def _extract_version(self, banner):
        """Extrahiert Versionsinfos aus Banner"""
        import re
        version_patterns = [
            r'(?i)version[\s:]+([0-9.]+)',
            r'(?i)v([0-9.]+)',
            r'([0-9]+\.[0-9]+\.[0-9]+)'
        ]
        
        for pattern in version_patterns:
            match = re.search(pattern, banner)
            if match:
                return match.group(1)
        return 'unknown'

    def os_detection(self, host):
        """Betriebssystem-Erkennung durch TTL-Analyse"""
        try:
            import subprocess
            import platform
            import re
            if platform.system().lower() == "windows":
                ping = subprocess.Popen(
                    ["ping", "-n", "1", host],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            else:
                ping = subprocess.Popen(
                    ["ping", "-c", "1", host],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            
            output = ping.communicate()[0].decode()
            ttl_match = re.search(r"TTL=(\d+)", output, re.IGNORECASE)
            
            if ttl_match:
                ttl = int(ttl_match.group(1))
                if ttl <= 64:
                    return "Linux/Unix"
                elif ttl <= 128:
                    return "Windows"
                elif ttl <= 255:
                    return "Cisco/Network Device"
            return "Unknown"
        except Exception as e:
            self.logger.error(f"OS-Erkennung fehlgeschlagen: {e}")
            return "Error" 

    def _check_default_credentials(self, host):
        """Überprüft auf Standard-Anmeldedaten"""
        try:
            # Basis-Implementation
            common_ports = [21, 22, 23, 80, 443, 3306, 8080]
            for port in common_ports:
                if port in self.port_scan(host):
                    return f"Potenziell unsichere Standard-Ports offen: {port}"
            return None
        except Exception as e:
            self.logger.error(f"Credentials-Check fehlgeschlagen: {e}")
            return None

    def _check_open_ports(self, host):
        """Überprüft auf unsichere offene Ports"""
        try:
            risky_ports = [23, 445, 135, 137, 138, 139]  # Bekannte unsichere Ports
            open_ports = self.port_scan(host)
            dangerous_ports = [p for p in open_ports if p in risky_ports]
            if dangerous_ports:
                return f"Unsichere Ports gefunden: {dangerous_ports}"
            return None
        except Exception as e:
            self.logger.error(f"Port-Check fehlgeschlagen: {e}")
            return None

    def _check_ssl_cert(self, host):
        """Überprüft SSL-Zertifikate"""
        try:
            import ssl
            import socket
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=host) as s:
                s.settimeout(self.timeout)
                try:
                    s.connect((host, 443))
                    cert = s.getpeercert()
                    # Einfache Überprüfung des Ablaufdatums
                    if cert and 'notAfter' in cert:
                        return None  # Zertifikat ist gültig
                except:
                    return "SSL-Zertifikat konnte nicht überprüft werden"
            return None
        except Exception as e:
            self.logger.error(f"SSL-Check fehlgeschlagen: {e}")
            return "SSL-Überprüfung fehlgeschlagen" 