species_name_map = {
    'Arboreal Species': ['Aboreal', 'Medium Sized Arboreal', 'Small Arboreal Sp.', 'Arboreal',
                     'Arboreal Sp. -Small', 'Arboreal Sp.'
                 'Arboreal Sp. Small', 'Arboreal Sp', 'Arboreal/Canopy',
                 'Unsure. Medium-Sized Detection Half-Way Up Tree.', 'Unsure If Anything',
                 'Detection Down Low On Trunk'],
    'Australian Brushturkey': ['Brush Turkey', 'Aus Brushturkeys'],
    'Bandicoot': ['Small Possible Bandicoot', 'Bandicoit', 'Bandicoot/ Pademelon?', 'Bandicoot?', 'Bandicoot/ Potoroo',
                  'Bandicoot (?)', 'Unknown (Bandicoot/Macropod?)', 'Unknown Mammal (Likely Bandicoot)',
                  'Small Unknown (Likely Bandicoot)', 'Rabbit/Bandicoot'],
    'Bat': ['Bats', 'Bats Or Birds'],
    'Bird': ['Roosting Birds?', 'Flock Of Birds', 'Bird Of Prey', 'Bird Of Prey On Nest', 'Bird On Nest', 'Birds',
             'Small-Ish Bird Or Sugar Glider? (In Flight)', 'Two Birds', 'Rock And Small Roosting Bird?',
             'Medium Sized Unknown Thermal - Ground/ Very Low Arboreal + Small Roosting Birds',
             'Large Bird, Likely Raptore E.G. Wedge-Tailed Eagle. Maybe Lyrebird',
             'Unsure, Medium Sized Mid-Canopy, Maybe Two Birds', 'Unidentified Birds (X2)', 'Unknown (Small Bird)',
             'Unknown (Likely Bird?)', 'Bird (Parrot)'],
    'Common Bronzewing': ['Bronzewings (X2) - Validated By Ground Crew'],
    'Cockatoo': ['Cockatoos And Warm Hollow', 'Cockatoos (X3)'],
    'Common Brushtail Possum': ['Brush Tail', 'Brush-Tailed Possum', 'Probable Brushtail Possum', 'Brushtail Possum',
                                'Brush-Tail Possum', 'Brush Tail Possum', 'Brushtail'],
    'Common Ringtail Possum': ['Ring Tail', 'Ring-Tailed Possum', 'Small Canopy - Ringtails?', 'Possum - Ringtail?',
                        'Possum (Ringtail?)', 'Possum - Ringtail ?', 'Probable Possum (Not Koala) - Ringtail?',
                        'Ringtail Possums', 'Ringtail And 3 Small Ground Mammals', 'Ringtail Possum ?',
                        'Possums (Ring-Tail?)', 'Ringtail'],
    'Cow': ['Cows'],
    'Cat': ['Feral Cat - Good Footage', '4 Legged Ground Mammal - Maybe Cat?', 'Feral Cat ?'],
    'Crimson Rosella': ['Crimson Roaella'],
    'Deer': ['Dear', 'Deer/Kangaroo'],
    'Dog': ['Dogs'],
    'Dusky Woodswallow': ['Dusky Woodswallows - Communal Roost'],
    'Eastern Grey Kangaroo': ['Eastern Grey', 'Macropod (Eastern Grey Kangaroos)', 'Macropod (Eastern Grey )',
                              'Grey Kangaroo'],
    'Feathertail Glider': ['Fethertail Glider', 'Feathertail', 'Feather-Tailed Glider Or Bird',
                           'Feathertail Gliders (X2)'],
    'Flying Fox': ['Flying-Fox', 'Flying Fox Fly-By', 'Single Video, Flying Fox Close', 'Pteropus Sp,'],
    'Glider': ['Glider - Gliding', 'Glider (Seen Airborne Only)', 'Glider Gliding', 'Glider Sp.', 'Glider And Wombat',
               'Small Glider', 'Large Glider (Greater Glider/Yellow Bellied Glider)', 'Small Other - Possible Glider'],
    'Goat': ['Goats', 'Goat Residual Body Heat Marks ?', 'Goats (Probable)', 'Goats Off Transect', 'Sheep Or Goat',
             'Goat (X3)', 'Sheep/Goat'],
    'Greater Glider': ['Greater Gliders', 'Greater Glider? Plus 2X Ground',
                       'Probable Greater Glider (Greater Or Yellow-Bellied) Plus Sugar Glider. Cool Footage',
                       'Greater Glider And Microbat', 'Possums ? Likely Greater Gliders',
                       'Greater Glider + 4 Uncertain Canopy (Possums, Gliders, Birds?)',
                       'Probable Greater Glider + Wombat', 'Greater Glider Moving Around Good Video',
                       'Greater Glider/ Brushie', 'Greater Glider/Brush-Tailed Possum', 'Greater Glider (X2)'],
    'Grey-headed Flying Fox': ['Grey Headed Flying Foxes', 'Grey Headed Flying Fox'],
    'Ground Species': ['2 Ground Unsure Medium Size - Review?', 'Unknown Ground', 'Macro? Ground',
                'Ground Macro?', 'Ground',
               'Ground. Not Animal?', 'Small Ground', 'Small Ground. Unknown', 'Small Ground Mammal', 'Ground Mammal',
               'Ground/ Shrub??', 'Ground Unknown', 'Small Ground/ Sub -Canopy Unknown', 'Ground, Macropod',
               'Ground/ Sub-Canopy? Possum/ Macropod?', 'Ground Unknonw', 'Small Ground Unknown',
               'Small Ground Sub-Canopy', 'Unknown Large Ground Detection At Base Of Tree - Sleeping Mammal/S',
               'Unknown Large Ground Detection Under Tree', 'Sleeping Large Mammal/S ?',
               'Unknown Small Ground Detection', 'Small Ground Detections', 'Ground Sp.', 'Small Ground Detection',
               'Ground Sp', 'Small', 'Unsure'],
    'Horse': ['Horses', 'Horse/Deer', 'Horse/Pig/Other', 'Horse/Pig'],
    'Koala': ['Pademelon/ Parma Wallaby (Plus Koala)', 'Koala (Same Koala)', 'Koala With Joey',
              'Unknown (Low Probability Koala)'],
    'Kreffts Glider': ['Krefts Glider'],
    'Kookaburra': ['Birds- Kookaburra'],
    'Lyrebird': ['Lyre Bird', 'Lyre Bied'],
    'Macropod': ['Small Macropod', 'Macropod?', 'Macropod ?', 'Ground Macropod', 'Macropods', 'Macropod (With Joey)',
                 'Macropod With Joey', 'Ground Prob Macropod', 'Maybe Macropod', 'Probably Macropod',
                 'Macropod And 2 Small Unkown', 'Macropod (X2)', 'Macropod (X3)', 'Macropod (?)', 'Macropod X3',
                 'Unknown, Medium (Sleeping Macropod?)', 'Wallaby/Potoroo?', 'Medium Unknown (Likely Macropod)',
                 'Macropod (Large, Grey Kangaroo From Size)', 'Macopod', 'Macropod And 2 Small Ground Detections'],
    'Magpie': ['Magpies'],
    'Microbat': ['Microbat In Flight'],
    'Mountain Brushtail Possum': ['Mountain Brush-Tailed Possum'],
    'Owl': ['Owl Sp.', 'Large Owl'],
    'Pademelon': ['Paddy Melon', 'Pademelon/ Parma Wallaby', 'Pademelon/Parma'],
    'Parrot': ['Parrot/ Cockatoos ?', 'Parrots'],
    'Potoroo': ['Potoroo?'],
    'Possum': ['Possum/ Glider', 'Possum / Glider', 'Possum And 2 Macropods', 'Possum / Glider Plus Wallaby',
               'Sub-Canopy Possum', 'Possum/S', 'Possum/ Greater Glider', 'Possum / Greater Glider',
               'Small Possum/ Glider', 'Possum?', 'Maybe Possum (Check Vid?)', 'Glider/ Possum, Unsure',
               'Possum/ Glider - Cant Get Lower To Confirm', 'Arboreal Unsure (Couldn’T Get Lower) Small, .Ikely Possum',
               'Possums', 'Small Arboreal, Cant Get Closer - Possum?', 'Possum Or Glider', 'Greater Glider/Possum',
               'Glider/Possum', 'Possum Sp.', 'Likely Possum', 'Possum/Glider', 'Possum Maybe Quoll?', 'Possum (X1)',
               'Possum (X2)', 'Unknown (Possum)', 'Possum (X3)', 'Unknown (Small, Likely Possum)',
               'Mammal (Likely Possum)', 'Small Unknown (Likely Possum)', 'Possum/Cat', 'Possum Or Tree Hollow',
               'Brushtail/Ringtail'],
    'Quoll': ['Quoll?', 'Quoll/Cat/Fox', 'Possum/Quoll'],
    'Red-necked Wallaby': ['Red Necked Wallaby'],
    'Short-eared Possum': ['Short-Eared Possum W/ Pouch Young'],
    'Sulfur-crested Cockatoo': ['Sulfur-Crested'],
    'Sooty Owl': ['Sooty Owl (Off Transecrt)'],
    'Sugar Glider': ['Sugar/ Squirrel Glider', 'Glider - Sugar/ Squirrel?'],
    'Rabbit': ['Rabbits'],
    'Termite Nest': ['Termite Mound', 'Termite', 'Arboreal Termite Nest?', 'Tree Growth/ Termites', 'Termite Or Hollow'],
    'Tree Hollow': ['Animal In Chimney Hollow', 'Hollow Possible Occupants', 'Tree Hollow To Rd',
                    'Vertical Hollow', 'Tree Hollow/Bee Hive/Temrites', 'Hollow Plus Maybe Unknown Arboreal', 'Hollow ?',
                    'Occupied Hollow', 'Chimney Tree Hollow', 'Chimney Hollow', 'Chimney Hollows', 'Stag Hollow',
                    'Occupied Hollow (In Fallen Stag)'],
    'Unkown': ['Unknown - Not A Koala', 'Unknown (X2)', 'Unknown (Fast?)', 'Unknown, Small',
               'Unvalidated', 'Validate Not Found', 'Small Mammal (X3)', '2X Small Mammal',
               'Small Mammal', 'Small Mammal (X2)', 'Small Unknown', 'Small Mammal Sp',
               'Smmall Mammal', 'Canopy', 'Mammal', 'Small Detection', 'Low'],
    'Yellow-bellied Glider': ['Glider (Prob Yellow-Bellied)',
                              'Several Gliders/ Possums. 4 Probable Yellow-Bellied Gliders? Below (One Seen In Flight) Plus One Sugar Glider At Eye Level',
                              'Yellow-Bellied Glider', 'Yellow Belly Glider'],
    'Yellow-tailed Black Cockatoo': ['Yellow-Tailed Black Cockatoos (Heard Call)',
                                     'Yellow-Tail Cockatoos (X8) - Validated'],
    'Wallaby': ['Wallaby And Other Small Ground Mammals?', 'Maybe Wallaby', 'Wallaby (Multiple)', 'Wallabies',
                'Wallaby (X2)'],
    'White-winged Chough': ['White Winged Chough'],
    'Wombat': ['2 Macropod 1 Wombat', 'Wombat And Wallaby', 'Wombat And Macropod?', 'Wombats',
               'Macropods And Wombat (3 Animals)', 'Wombat/ Deer?', 'Wombat?', 'Wombat Or Deer?',
               'Uncertain, Maybe Wombat', 'Pig Or Wombat', 'Unknown (Wombat)', 'Wombat (X2)',
               'Wombat And Small Unidentified Ground']
}

to_remove = ['Dummy', 'Human', 'Bulge On Branch', 'Human', 'No Detection', 'Uncertain',
             'Cannot Tell? Wasp Nest?', 'Possibly Hot Rocks', 'Rocks?', 'Rock', 'Maybe Rock?', 'Hbt',
             'Ns West Start Terrible Reception, Difficult To Descend For Closer Inspection',
             'Other - Add Details In Notes', 'NaN']

doubles = ['2 Macropod 1 Wombat', 'Possum And 2 Macropods', 'Wombat And Wallaby',
           'Pademelon/ Parma Wallaby (Plus Koala)', 'Greater Glider? Plus 2X Ground',
           'Several Gliders/ Possums. 4 Probable Yellow-Bellied Gliders? Below (One Seen In Flight) Plus One Sugar Glider At Eye Level',
           'Greater Glider And Microbat', 'Greater Glider + 4 Uncertain Canopy (Possums, Gliders, Birds?)',
           'Probable Greater Glider + Wombat', 'Wombat And Macropod?',
           'Medium Sized Unknown Thermal - Ground/ Very Low Arboreal + Small Roosting Birds',
           'Macropods And Wombat (3 Animals)', 'Ringtail And 3 Small Ground Mammals',
           'Glider And Wombat', 'Wombat And Small Unidentified Ground']

probability_map = {
    'Low': ['0%'],
    'Med': ['Medium', 'Probable', 'med', 'medium'],
    'High': ['high', 'Med/High'],
    '100%': ['Certain', 'Definite']
}