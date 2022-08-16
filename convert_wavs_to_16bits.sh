for f in $(find ./ -name '*.wav'); do 
ffmpeg -i $f -acodec pcm_s16le -ar 22050 ${f%.wav}z.wav; 
mv -f ${f%.wav}z.wav $f;
done
