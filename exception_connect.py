'''The connect() call will sometimes fail with an exception. Additional information about
an exception can be obtained by running the connect within a try-catch block as shown:'''

import dronekit
import socket
# import exceptions


try:
    dronekit.connect('REPLACE_connection_string_for_your_vehicle', heartbeat_timeout=15)

# Bad TCP connection
except socket.error:
    print ('No server exists!')

# Bad TTY connection
# except exceptions.OSError as e:
#     print ('No serial exists!')

# API Error
except dronekit.APIException:
    print ('Timeout!')

# Other error
except:
    print ('Some other error!')