# verion 0.1.0
# proto-flow

current_step = None

flow = {
    "steps" : {
        "1": {"keys": {

        }, "conditions": {

        },
        "next_step": "2"
        },
        "2": {"keys": {

        }, "conditions": {

        },
        "next_step": "3"
        },
        "3": {"keys": {

        }, "conditions": {

        },
        "next_step": "4"
        },
        "4": {"keys": {

        }, "conditions": {

        },
        "next_step": "5"
        },
        "5": {"keys": {

        }, "conditions": {

        },
        "next_step": "6"
        },
        "6": {"keys": {

        }, "conditions": {

        },
        "next_step": "0"
        },
    }
}

def start_flow():
    global current_step
    current_step = "1"

def next_step(step_id):
    global current_step
    step = flow["steps"][step_id]
    current_step = step["next_step"]

def run_step(step_id):
    step = flow["steps"][step_id]
    print(step, step["keys"], "next_step: " + str(step["next_step"]))

def is_not_end_of_flow(step_id):
    step = flow["steps"][step_id]
    if step["next_step"] == "0":
        print("You reached the end of the flow!")
        return False
    return True

if __name__ == "__main__":
    start_flow()
    while is_not_end_of_flow(current_step):
        run_step(current_step)
        next_step(current_step)