

import cv2
from pyzbar.pyzbar import decode

def read_barcode():
    # Open the camera (you may need to adjust the camera index)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Decode barcode
        barcodes = decode(frame)
        if barcodes:
            barcode_data = barcodes[0].data.decode("utf-8")
            print("Barcode:", barcode_data)
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data

        # Display the frame
        cv2.imshow("Barcode Reader", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    barcode_data = read_barcode()
    print("Barcode Data:", barcode_data)
