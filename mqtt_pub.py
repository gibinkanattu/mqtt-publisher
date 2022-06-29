import paho.mqtt.client as mqtt 
import json,sys,time,argparse,logging

def parse_argv(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--conf", required=True)
    parser.add_argument("--data", required=True)
    args = parser.parse_args(argv)
    args = vars(args)    
    return args

def main():
    try:
        client = mqtt.Client()
        args = parse_argv(sys.argv[1:])
        conf_file=args.get("conf")
        with open(conf_file,"r") as fp:
            params   = json.load(fp)
            broker = params.get("broker")
            topic  = params.get("topic")
            port   = params.get("port")
            publish_interval      = params.get("publish_interval")
            qos    = params.get("qos")
            log    = params.get("log")
        logging.basicConfig(filename=log, level=logging.ERROR)
        try:
            client.connect(broker,port)
            data_file = args.get("data")
            with open(data_file,"r") as fp:
                data=json.load(fp)
                data=json.dumps(data)
            flag = True
            while True:
                client.loop_start()
                client.publish(topic,payload=data,qos=qos)
                if flag:
                    logging.info(data)
                    flag=False
                time.sleep(publish_interval)
        except Exception as e:
            logging.error(e)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()