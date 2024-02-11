import os

def main():
    filename = "images/disc.png"
    with open(filename, "rb") as image_file:
        image_file.seek(18)
        width, height = int.from_bytes(image_file.read(4), byteorder='little'), int.from_bytes(image_file.read(4), byteorder='little')
        image_file.seek(28)
        bpp = int.from_bytes(image_file.read(2), byteorder='little')
        bmpdataoff = int.from_bytes(image_file.read(4), byteorder='little')
        image_file.seek(bmpdataoff)

        image = []
        for _ in range(height):
            image.append(list(image_file.read(width * 3))

    hist = [0] * 256
    for i in range(height):
        for j in range(width):
            # Ensure that the pixel value is within the [0, 255] range
            pixel_value = min(max(image[i][j], 0), 255)
            hist[pixel_value] += 1

    nodes = sum(1 for freq in hist if freq > 0)
    p = min(freq / (height * width) for freq in hist if freq > 0)
    maxcodelen = 0
    while 1 / p > maxcodelen:
        maxcodelen += 1

    class PixFreq:
        def __init__(self):
            self.pix = 0
            self.freq = 0
            self.left = None
            self.right = None
            self.code = []

    huffcodes = [PixFreq() for _ in range(nodes)]
    pix_freq = [PixFreq() for _ in range(2 * nodes - 1)]

    j = 0
    totpix = height * width
    for i in range(256):
        if hist[i] != 0:
            huffcodes[j].pix = i
            pix_freq[j].pix = i
            tempprob = hist[i] / totpix
            huffcodes[j].freq = tempprob
            pix_freq[j].freq = tempprob
            j += 1

    huffcodes = sorted(huffcodes[:nodes], key=lambda x: x.freq, reverse=True)
    nextnode = nodes

    while len(huffcodes) > 1:
        sumfreq = huffcodes[-1].freq + huffcodes[-2].freq
        pix_freq[nextnode].pix = huffcodes[-1].pix + huffcodes[-2].pix
        pix_freq[nextnode].freq = sumfreq
        pix_freq[nextnode].left, pix_freq[nextnode].right = huffcodes[-2], huffcodes[-1]
        pix_freq[nextnode].code = []
        i = nextnode - 1
        while sumfreq <= huffcodes[i].freq:
            i -= 1
        huffcodes.insert(i + 1, pix_freq[nextnode])
        huffcodes.pop()

        nextnode += 1

    left, right = '0', '1'

    for i in range(len(pix_freq) - 1, nodes - 1, -1):
        if pix_freq[i].left:
            pix_freq[i].left.code = pix_freq[i].code + left
        if pix_freq[i].right:
            pix_freq[i].right.code = pix_freq[i].code + right

    encoded_image = ''.join(pix_freq[huffcodes.index(x)].code for x in image)
    
    with open("encoded_image.txt", "w") as imagehuff:
        imagehuff.write(encoded_image)

    print("Huffman Codes:")
    print("Pixel values -> Code")
    for node in huffcodes:
        print(f"{node.pix: >3} -> {''.join(node.code)}")

    avgbitnum = sum(node.freq * len(node.code) for node in huffcodes)
    print(f"Average number of bits: {avgbitnum}")

if __name__ == "__main__":
    main()