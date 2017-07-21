import logging
import os
from django.db import transaction
from ConfigParser import SafeConfigParser
from datastore.imageRepository.LocalRepository import LocalRepository
from datastore.models.NfImage import VNF_Image
from datastore.services import NfTemplateService


parser = SafeConfigParser()
parser.read(os.environ["DATASTORE_CONFIG_FILE"])
logging.basicConfig(filename=parser.get('logging', 'filename'), format='%(asctime)s %(levelname)s:%(message)s',
                    level=parser.get('logging', 'level'))
repository = parser.get('repository', 'repository')
if repository == "LOCAL_FILES":
    imagesDir = parser.get('General', 'IMAGE_DIR')
    imageRepo = LocalRepository(imagesDir)


def getImage(vnf_id):
    """
    Get the disk image of a VNF
    """
    try:
        (wrapper, fileLen) = imageRepo.getImage(vnf_id)
        return wrapper, fileLen
    except:
        return None


def deleteImage(vnf_id):
    """
    Remove a disk image for a VNF
    """
    try:
        state = VNF_Image.objects.get(vnf_id=str(vnf_id)).image_upload_status
        if state == VNF_Image.COMPLETED:
            imageRepo.deleteImage(vnf_id)
        return True
    except:
        return False


def updateImage(vnf_id, image):
    try:
        imageRepo.storeImage(vnf_id, image)
        return True
    except:
        return False


#Template reference API
def getTemplate(vnf_id):
    found_image = VNF_Image.objects.filter(vnf_id=vnf_id)
    if len(found_image) == 0:
        return None, "The instance of the vnf with ID " + vnf_id + " does not exist"
    template = found_image[0].template
    if template is None:
        return None, ""
    return template, "Ok"


@transaction.atomic
def deleteTemplate(vnf_id):
    vnf = VNF_Image.objects.filter(vnf_id=vnf_id)
    if len(vnf) != 0 and vnf[0].template is not None:
        vnf.update(template=None)
        return True
    return False


@transaction.atomic
def updateTemplate(vnf_id, template_id):
    vnf = VNF_Image.objects.filter(vnf_id=vnf_id)
    if len(vnf) == 0:
        return False, "The instance of the vnf with ID " + vnf_id + " does not exist"
    templateObj = NfTemplateService.getTemplateObject(template_id=template_id)
    if templateObj is None:
        return False, "The template with ID " + template_id + " does not exist"
    vnf.update(template_id=templateObj)
    return True, "Ok"
