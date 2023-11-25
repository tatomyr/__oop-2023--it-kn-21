<script setup>
</script>

<template>
  <header>
    <div class="wrapper">
      <RouterLink to="/search">
        <button class="search btn-standard"><img src="../assets/search.svg" alt=""></button>
      </RouterLink>
      <h6>PLAYING NOW</h6>
      <RouterLink to="/playlist">
        <button class="menu btn-standard"><img src="../assets/menu.svg" alt=""></button>
      </RouterLink>
    </div>
  </header>
  <main>
      <div class="song-cover">
          <img :src="music.cover" alt="Song Cover">
      </div>
      <div class="song-info">
          <h1 class="song-title">{{ music.title }}</h1>
          <h2 class="song-artist">{{ music.artist }}</h2>
      </div>
      <div class="song-bar">
          <div class="song-duration">
              <span class="current">{{ convertTime(duration.current) }}</span>
              <span class="total">{{ convertTime(duration.total) }}</span>
          </div>
          <input type="range" class="progress-bar" :max="duration.total" v-model="duration.current" @input="rewindAudio()">
      </div>
      <!-- <audio id="audioPlayer" controls :src="music.file" @ended="getMusicData(1)" @timeupdate="timeupdate()"></audio> -->
      <div class="song-controls">
          <button class="previous btn-standard" @click="getMusicData(-1)"><img src="../assets/fast-forward.svg" alt=""></button>
          <button class="play" :class="{ 'btn-standard': this.player.paused }"  @click="play()">
            <img v-if="this.player?.paused" src="../assets/play.svg" alt="">
            <img v-if="!this.player?.paused" src="../assets/pause.svg" alt="">
          </button>
          <button class="next btn-standard" @click="getMusicData(1)"><img src="../assets/fast-forward.svg" alt=""></button>
      </div>
      <div class="song-volume">
          <img src="" alt="">
          <input type="range" class="volume-slider" v-model="volume" max="1" step="0.01" @input="changeVolume()">
          <img src="" alt="">
      </div>
  </main>

</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
  name: 'MusicPlayer',
  props: {
    url: String
  },
  data() {
    return {
      player: null,
      music: {
        title: 'Song Title',
        artist: 'Artist Name',
        cover: '',
        file: 'src/assets/song.mp3',
        max: 9,
      },
      duration: {
        current: 0,
        total: 0,
      },
      position: 0,
      volume: 1, 
    };
  },
  methods: {
    getMusicData(shift) {
      var position = this.position + shift;
      if (position < 0) {
        position = this.music.max;
      }
      else if (position > this.music.max) {
        position = 0;
      }
      this.position = position;
      const path = this.url + 'getMusicData?pos=' + position;
      axios.get(path)
        .then((res) => {
          this.music = res.data;
          this.duration.total = res.data.duration
          if (this.player) {
            this.player.pause();
          }
          this.player = new Audio(this.music.file);
          this.player.addEventListener('timeupdate', this.timeupdate, false);
          this.player.addEventListener('ended', () => {
            this.getMusicData(1);
            this.duration.current = 0;
          }, false);
          this.play();
        })
        .catch((error) => {

          console.error(error);
        });
    },
    play() {
      if (this.player.paused) {
        this.player.play();
        
        this.duration.total = this.music.duration;
      } else {
        this.player.pause();
      }
    },
    rewindAudio() {
      this.player.currentTime = this.duration.current;
    },
    timeupdate() {
      this.duration.current = this.player.currentTime;
      
    },
    convertTime(time) {
      const min = Math.floor(time / 60);
      const sec = Math.floor(time % 60);
      time = `${min.toString()
        .padStart(2, '0')}:${sec.toString()
        .padStart(2, '0')}`;
      return time
    },
    changeVolume() {
      this.player.volume = this.volume;
    }
  },
  created() {
    console.log(this.url);
    if(this.$route.params.position) {
      console.log(this.$route.params.position);
      this.position = parseInt(this.$route.params.position);
    }
    this.getMusicData(0);
  },
  unmounted() {
    if(this.player) {
      this.player.pause();
      this.player = null;
    }
  }
};
</script>

