# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
Goal1 = '32'
Goal2 = '54'
scorers = player1 + ' ' + str(Goal1) + ', ' + player2 + ' ' + str(Goal2)
report = f'{player1} scored in the {Goal1}nd minute \n{player2} scored in the {Goal2}th minute'
player = 'Frank Rijkaard'
find_space = player.find(' ')
first_name = player[:int(find_space)]
last_name = player[int(find_space)+1:]
last_name_len = len(last_name)
name_short = player[0] + '. ' + f'{last_name}'
chant = f'{first_name}! ' * int(len(first_name)-1) + f'{first_name}!'
good_chant = chant[-1] != ' '

vars = [scorers, report, player, first_name, last_name, last_name_len, name_short, chant, good_chant]
for v in vars: print(v)