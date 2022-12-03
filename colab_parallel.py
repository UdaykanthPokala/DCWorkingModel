from train import run
import time, threading


def parallel(yaml_file, epoch):
    run(data=yaml_file, epochs=epoch, device=0)



if __name__ =="__main__":
    start_time = time.time()
    t1 = threading.Thread(target=parallel, args=['/content/yolov5/train1.yaml', 10,])
    t1.start()
    t2 = threading.Thread(target=parallel, args=['/content/yolov5/train2.yaml', 5, ])
    t2.start()
    t1.join()
    t2.join()
    print("Total Time taken for seqential", time.time() - start_time)