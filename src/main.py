from notebook import readVideoCapture
def main():
    file = "multiball"
    path = f'../data/{file}_cropped_610px.mkv'
    capture = readVideoCapture(path)


if __name__ == "__main__":
    main()

