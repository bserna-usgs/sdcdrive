'''
Shellout - Attach Disk Image
'''
import os

# First remove any traces
def remove_old_work():
    # If there's still files within the image, rm
    if os.path.exists('/Volumes/SDC\ Drive'):
        try:
            os.system('rm -rf /Volumes/SDC\ Drive')
        except Exception as e:
            print("Error in removing the existing Volume ")
            print(e)


def attach_image():
    os.system("hdiutil attach sdc_beta.dmg;")
    print('Attaching SDCDrive mount...')

    if os.path.exists('/Volumes/SDC Drive'):
        amt = len(os.listdir('/Volumes/SDC Drive'))
        print(amt)
        if amt > 0:
            try:
                print("Removing all previous files...")
                os.system('rm -rf /Volumes/SDC\ Drive/*')
                print("Directory cleaned")
            except Exception as e:
                print(e)
