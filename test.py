

text = "blur:3|grayscale"

id = text.split('|')

print(id[1])


# save :
# elif '--filters' in args:
#     pos = args.index('--filters')
#     if '--filters' == args[-1]:
#         print('Please add filter to apply')
#     else:
#         id = args[pos+1]
#         filtre = id.split('|')
#         for item in filtre:
#             if item.startswith('grayscale'):
#                 print('grayscale done')
#             elif item.startswith('zeteam'):
#                 print('zeteam done')
#             elif item.startswith('blur'):
#                 number = item.split(':')
#                 try:
#                     intensity = int(number[1])
#                     print(f'Intensity of the filter: {intensity}')
#                 except IndexError:
#                     print('Please enter a value as filter intensity')
#                 except ValueError:
#                     print('Please enter an int as filter intensity')
#             elif item.startswith('dilate'):
#                 number = item.split(':')
#                 try:
#                     intensity = int(number[1])
#                     print(f'Intensity of the filter: {intensity}')
#                 except IndexError:
#                     print('Please enter a value as filter intensity')
#                 except ValueError:
#                     print('Please enter an int as filter intensity')
#             elif item.startswith('message'):
#                 number = item.split(':')
#                 try:
#                     msg = str(number[1])
#                     print(f'Message of the filter: {msg}')
#                 except IndexError:
#                     print('Please enter a message as filter value')