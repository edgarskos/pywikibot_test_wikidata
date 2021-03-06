import argparse
import csv
import pywikibot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript_file", help="the file, that contains the transcript information")
    parser.add_argument("strain_name", help="please type in the correct name of the strand")
    
    args = parser.parse_args()

    bab = BacterialAnnotationBot(args.transcript_file, args.strain_name)

    #bab.read_csv()

    bab.check_item_existence()

    strain = Strain(args.strain_name)

    strain.show_strain_name()

    strain.create_strain_item()

class BacterialAnnotationBot():

    def __init__(self, transcript_file, strain_name):
        self.transcript_file = transcript_file
        self.strain_name = strain_name

    def read_csv(self):
        transcript_file = self.transcript_file
        with open(transcript_file) as csvfile:
            transcript_dict = csv.DictReader(csvfile, delimiter="\t")
            for row in transcript_dict:
                site = pywikibot.Site("en", "TillsWiki")
                repo = site.data_repository()

                data = {
                    'labels': {
                        'en': {
                            'language': 'en',
                            'value': row['Name']
                        }
                    },
                    'descriptions': {
                        'en': {
                            'language': 'en',
                            'value': 'bacterial transcript found in ' + self.strain_name
                        }
                    }
                }

                item = pywikibot.ItemPage(site)
                item.editEntity(data)


                
                #print(row['strain'],"\n")
                #print(row)
               
    def check_item_existence(self):
        transcript_file = self.transcript_file
        with open(transcript_file) as csvfile:
            transcript_dict = csv.DictReader(csvfile, delimiter="\t")
            for row in transcript_dict:
                site = pywikibot.Site("en", "TillsWiki")
                existing_item = pywikibot.ItemPage(site, row['Name'])
                print(existing_item.id)
                
                
class Strain():
    
    def __init__(self, strain_name):
        self.strain_name = strain_name

    def show_strain_name(self):
        print(self.strain_name)

    def create_strain_item(self):
        site = pywikibot.Site("en", "TillsWiki")
        repo = site.data_repository()

        data = {
            'labels': {
                'en': {
                    'language': 'en',
                    'value': self.strain_name,
                }
            },
            'descriptions': {
                'en': {
                    'language': 'en',
                    'value': 'bacterial strain'
                }
            }
        }

        item = pywikibot.ItemPage(site)
        item.editEntity(data)
        
        #claim = pywikibot.Claim(site, u'P6')
        #target = pywikibot.ItemPage(site, u"Q9")
        #claim.setTarget(target)
        #item.addClaim(claim)

    
                
main()
