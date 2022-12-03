from train import run
import time


def sequential(yaml_file, epoch):
    run(data=yaml_file, epochs=epoch, device=0)



if __name__ =="__main__":
    start_time = time.time()
    sequential('train1.yaml',10 )
    sequential('train2.yaml',10 )
    print("Total Time taken for seqential", time.time() - start_time)