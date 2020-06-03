import argparse
import blur_1
import blur_2
import blur_3
import blur_4

parser = argparse.ArgumentParser()

parser.add_argument("method",
                    help="input which method to use for blurring. Accepted inputs are 1,2,3 or 4. 1=regular python, "
                         "2=numpy, 3=numba, 4=cython",
                    type=int, choices=[1, 2, 3, 4])
parser.add_argument("src", help="filepath for image")
parser.add_argument("-dst", "--destination", help="optional, name for blurred image")

args = parser.parse_args()

if args.method == 1:
    blur_1.run(args.src, args.destination)
elif args.method == 2:
    blur_2.run(args.src, args.destination)
elif args.method == 3:
    blur_3.run(args.src, args.destination)
elif args.method == 4:
    blur_4.run(args.src, args.destination)
