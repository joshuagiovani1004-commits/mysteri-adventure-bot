import random
import time
import sys


SWORD_ART = r"""
	   />_________________________________
[########[]_________________________________>
	   \>
"""

SKULL_ART = r"""
	   .-.
	  (o.o)
	   |=|
	  __|__
	//.=|=.\\
   // .=|=. \\
   \\ .=|=. //
	\\(_=_)//
	 (:| |:)
	  || ||
	  () ()
	  || ||
	  || ||
	 ==' '==
"""


DELAY = 0.5
DAMAGE = 20
START_LIFE = 100


def slow_print(text, delay=DELAY):
	print(text)
	time.sleep(delay)


def prompt_choice(prompt, options):
	slow_print(prompt)
	for i, opt in enumerate(options, 1):
		slow_print(f"  {i}. {opt}")
	choice = input('Pilih nomor: ').strip()
	try:
		idx = int(choice) - 1
		if 0 <= idx < len(options):
			return idx
	except ValueError:
		pass
	# fallback: try match by text
	choice_l = choice.lower()
	for i, opt in enumerate(options):
		if choice_l in opt.lower():
			return i
	return None


def lembah_coding(life):
	slow_print('\nKamu berjalan ke Lembah Coding — barisan laptop berkilau di bawah kabut.')
	event = random.random()
	if event < 0.6:
		slow_print('Kamu menemukan mentor yang memberi petunjuk penting. Kamu unggul!')
		return life, True
	else:
		slow_print('Sebuah Bug misterius muncul dan menggigit kode kamu!')
		life -= DAMAGE
		slow_print(f'Nyawamu berkurang {DAMAGE}. Sisa nyawa: {life}')
		return life, False


def gunung_bug(life):
	slow_print('\nKamu mendaki Gunung Bug — angin dingin dan error stack yang curam.')
	event = random.random()
	if event < 0.4:
		slow_print('Kamu berhasil mendebug puncak dan menemukan Pedang Algoritma!')
		slow_print(SWORD_ART)
		return life, True
	else:
		slow_print('Kamu terpeleset ke jurang Exception dan terluka parah!')
		life -= DAMAGE
		slow_print(SKULL_ART)
		slow_print(f'Nyawamu berkurang {DAMAGE}. Sisa nyawa: {life}')
		return life, False


def play_game():
	slow_print('=== Mysteri Adventure Bot ===')
	life = START_LIFE
	slow_print(f'Kondisi awal: Nyawa = {life}\n')

	# small narrative loop
	while life > 0:
		idx = prompt_choice('Pilih jalur petualanganmu:', ['Lembah Coding', 'Gunung Bug'])
		if idx is None:
			slow_print('Pilihan tidak dikenali. Coba lagi.')
			continue

		if idx == 0:
			life, success = lembah_coding(life)
		else:
			life, success = gunung_bug(life)

		# random bonus/malus
		luck = random.randint(1, 10)
		if luck >= 9 and success:
			slow_print('Keberuntungan berpihak padamu! Kamu menemukan ramuan penyembuh (+20 nyawa).')
			life += 20
			slow_print(f'Sisa nyawa: {life}')
		elif luck <= 2 and not success:
			slow_print('Nasib buruk melengkapi malapetaka — serangan ganda! (-20 nyawa)')
			life -= DAMAGE
			slow_print(f'Sisa nyawa: {life}')

		# check win/lose
		if life <= 0:
			slow_print('\nKamu tewas dalam petualangan...')
			slow_print(SKULL_ART)
			break

		if success and random.random() < 0.5:
			slow_print('\nKemenangan! Kamu menaklukan rintangan dan selamat pulang.')
			slow_print(SWORD_ART)
			break

		slow_print('\nPetualangan berlanjut...')

	slow_print('\n=== Akhir Petualangan ===')


def main():
	while True:
		play_game()
		again = input('\nMain lagi? (y/n): ').strip().lower()
		if again != 'y':
			slow_print('Terima kasih telah bermain. Sampai jumpa!')
			break


if __name__ == '__main__':
	main()

