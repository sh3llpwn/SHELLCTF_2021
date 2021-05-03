FROM patched_cryptsetup:latest

RUN rm -rf /root/*.deb

RUN echo "Remember Luke, You can't trust anyone at this point.." >> /root/notes.txt 
RUN echo "Be sure to make all the changes inside the secure encrypted container" >> /root/notes.txt
RUN echo "luke" > /root/.passwd
RUN echo "354055bd7b1e30c6af4638d33298c296d78cc462e865c6b460eaa6adcb4a113f  disk.img" > /root/sha256sum

COPY disk.img /root/disk.img