from security import assess_security


# -----------------------------------------
# Normal device
# -----------------------------------------

normal_device = {

    "device": "R1",

    "latency": 25,

    "packet_loss": 0.5,

    "cpu": 45,

    "memory": 50,

    "bandwidth": 50,

    "interface_errors": 1,

    "traffic": 60
}


# -----------------------------------------
# Possible security event
# -----------------------------------------

security_device = {

    "device": "R3",

    "latency": 90,

    "packet_loss": 12,

    "cpu": 85,

    "memory": 70,

    "bandwidth": 95,

    "interface_errors": 1,

    "traffic": 98
}


print("\n==============================")
print(" SECURITY ASSESSMENT")
print("==============================\n")


print("NORMAL DEVICE:")

print(
    assess_security(normal_device)
)


print("\nPOTENTIAL SECURITY EVENT:")

print(
    assess_security(security_device)
)
