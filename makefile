#one might run these in parallel to spice up race condidion
all:
	python whack.py &
	python whack.py &
clean:
	rm adsf*
