import os
import sys
from datetime import datetime

import numpy
import pyfits as fits
from PIL import Image, ImageDraw, ImageFont
from scipy.misc import toimage


def set_header(fitname):
    # Abrindo o arquivo
    fits_file = fits.open(fitname)
    # Escrevendo o Header
    # Can't get the temperature because have a locker locking shooter process
    # fits_file[0].header["TEMP"] = tuple(get_temperature())[3]
    fits_file[0].header["DATE"] = datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')

    # Criando o arquivo final
    try:
        print("Tricat of set_header")
        # Fechando e removendo o arquivo temporario
        # fits_file.flush()
        fits_file.close()
    except OSError as e:
        print(fitname)
        print("Exception ->" + str(e))


def save_tif(img, newname):
    print("Opening filename")
    try:
        print("tricat of save_tif")

        try:
            if sys.platform.startswith("linux"):
                imgarray = numpy.array(img, dtype='uint16')
            elif sys.platform.startswith("win"):
                imgarray = numpy.array(img, dtype='int16')
        except Exception as e:
            print(e)

        im3 = Image.fromarray(imgarray)
        im3.save(newname)

        '''
        salvar tif via tifffile.py
        img2 = numpy.array(img, dtype='uint16')
        skimage.io.imsave(newname, img2, plugin='tifffile')
        '''
    except Exception as e:
        print("Exception -> {}".format(e))


def save_png(img, newname, get_level1, get_level2):
    '''
    :param filename: nome do arquivo fit criado
    :param newname: nome do arquivo png criado a partir do fit
    :param get_level1: Image contrast: bottom level
    :param get_level2: Image contrast: top level
    :return: arquivo fit e png. Arquivo .png redimensionado para 512X512, com a lib PIL se desenha na imagem os \
    seguintes:
    Nome do observatorio, nome do filtro, data e horario.
    '''
    print("Opening filename")
    try:
        print("tricat of save_png")
        img_aux = toimage(img)
        im2 = img_aux

        variavel = get_level(im2, get_level1, get_level2)

        im2 = bytscl(img, variavel[1], variavel[0])
        img_aux.save(newname)

        im3 = toimage(im2)
        im3.save(newname)

        resize_image_512x512(newname)
        draw_image(newname)

    except Exception as e:
        print("Exception -> {}".format(e))


def retorna_imagem(name_png):
    """
    :param name_png: recebe imagem png
    :return:
    """
    img2 = Image.open(name_png)
    img2.show()


def resize_image_512x512(name_png):
    '''
    :param name_png: recebe imagem png
    :return: modifica tamanho para 512x512
    '''
    img = Image.open(name_png)
    resized_img = img.resize((int(512), int(512)))
    #resized_img = ImageOps.autocontrast(resized_img, 2)
    resized_img.save(name_png)


def draw_image(name_png):
    '''
    :param name_png: recebe imagem png
    :return: escreve valores na imagem e salva
    '''
    hora_img, data_img = get_date_hour_image(name_png)
    filter_img, observatory_img = get_filter_observatory(name_png)

    img = Image.open(name_png)

    fontsFolder = '/usr/share/fonts/truetype'
    times_nr_Font = ImageFont.truetype(os.path.join(fontsFolder, 'Times_New_Roman_Bold.ttf'), 16)

    draw = ImageDraw.Draw(img)
    draw.text((10, 10), observatory_img, fill='white', font=times_nr_Font)
    draw.text((470, 10), filter_img, fill='white', font=times_nr_Font)
    draw.text((420, 490), hora_img, fill='white', font=times_nr_Font)
    draw.text((10, 490), data_img, fill='white', font=times_nr_Font)
    del draw

    img.save(name_png)
    #mostra imagem unicamente
    #img.show()


def bytscl(array, max = None, min = None, nan = 0, top=255):
    # see http://star.pst.qub.ac.uk/idl/BYTSCL.html
    # note that IDL uses slightly different formulae for bytscaling floats and ints.
    # here we apply only the FLOAT formula...

    if max is None: max = numpy.nanmax(array)
    if min is None: min = numpy.nanmin(array)

    # return (top+0.9999)*(array-min)/(max-min)
    return numpy.maximum(numpy.minimum(
        ((top + 0.9999) * (array - min) / (max - min)).astype(numpy.int16)
        , top), 0)


def get_level(im2, sref_min, sref_max):
    '''
    :param im2: imagem tipo float
    :param sref_min: nivel de referencia normalizado
    :param sref_max: nivel de referencia normalizado
    :return: limites inferior e superior da imagem para exibição na tela, baseado nos niveis de referencia.
    '''
    #
    x_min, x_max = numpy.min(im2), numpy.max(im2)

    # bin_size precisa ser 1 para analisar ponto à ponto
    bin_size = 1
    x_min = 0.0

    nbins = numpy.floor(((x_max - x_min) / bin_size))

    try:
        hist, bins = numpy.histogram(im2, int(nbins), range=[x_min, x_max])

        sum_histogram = numpy.sum(hist)

        sref = numpy.zeros(2)
        sref[0] = sref_min
        sref[1] = sref_max

        res_sa = numpy.zeros(len(hist))

        sa = 0.
        for i in range(len(hist)):
            sa += hist[i]
            res_sa[i] = sa

        res_sa2 = res_sa.tolist()
        res = res_sa[numpy.where((res_sa > sum_histogram * sref[0]) & (res_sa < sum_histogram * sref[1]))]
        nr = len(res)

        sl0 = res_sa2.index(res[0])
        sl1 = res_sa2.index(res[nr - 1])
        slevel = [sl0, sl1]
    except Exception as e:
        print("Exception get_level ->" + str(e))
        print("slevel = [10, 20]")
        slevel = [10, 20]

    return slevel


def get_date_hour(tempo):
    data = tempo[0:4] + "_" + tempo[4:6] + tempo[6:8]
    hora = tempo[9:11] + ":" + tempo[11:13] + ":" + tempo[13:15]

    return data, hora


def get_date_hour_image(tempo):
    hora_img = tempo[-10:-8] + ":" + tempo[-8:-6] + ":" + tempo[-6:-4] + " UT"
    data_img = tempo[-13:-11] + "/" + tempo[-15:-13] + "/" + tempo[-19:-15]

    return hora_img, data_img


def get_filter_observatory(name):
    name_aux = name.split('/')[-1]
    name_filter = name_aux.split('_')[0]
    name_observatory = name_aux.split('_')[1]

    return name_filter, name_observatory


def get_observatory(name):
    name_aux = str(name).split(',')[1]
    name_aux = name_aux.replace("\'", "")
    name_aux = name_aux.replace(" ", "")

    return name_aux
