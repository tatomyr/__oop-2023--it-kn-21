<template>
    <div class="container">
        <header>
            <div class="wrapper">
                <RouterLink to="/">
                    <button class="back btn-standard"><img src="../assets/return.svg" alt=""></button>
                </RouterLink>
                <h6>SEARCH</h6>
                <RouterLink to="/playlist">
                    <button class="menu btn-standard"><img src="../assets/menu.svg" alt=""></button>
                </RouterLink>
            </div>
        </header>
        <main>
            <div class="search-container">
                <form @submit.prevent="getMusicData">
                    <input type="text" placeholder="Enter your request" class="search-input" v-model="request">
                </form>
            </div>
            <div class="song-container">
                <div class="search-wrapper" v-for="music in musics" :key="music.id">
                    <div class="search-cover">
                        <img :src="music.album.cover_medium" alt="">
                    </div>
                    <div class="song-info">
                        <h3 class="song-name">{{ music.title }}</h3>
                        <h4 class="song-artist">{{ music.artist.name }}</h4>
                    </div>
                    <div class="download">
                        <button class="btn-standard" @click="download([music.id, music.title])"
                                :disabled="disabled.includes(music.id)">
                            <img src="../assets/download.svg" alt="">
                        </button>
                    </div>
                </div>
            </div>
        </main>
        <vue-basic-alert 
       :duration="300" 
       :closeIn="3000" 
       ref="alert" />
    </div>
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

import VueBasicAlert from 'vue-basic-alert'

export default {
    name: 'SearchComponent',
    props: {
        url: String
    },
    data() {
        return {
            musics: [],
            request: '',
            disabled: []
        };
    },
    methods: {
        getMusicData() {
            const path = this.url + 'search?query=' + this.request + '/';
            axios.get(path)
                .then((res) => {
                this.musics = res.data;
            })
                .catch((error) => {
                console.error(error);
            });
        },
        download(arr){
            var [songId, title] = arr;
            this.disabled.push(songId);
            const path = this.url + 'download';
            this.$refs.alert
                .showAlert(
                    'info', 
                    'Start downloading the song "' + title + '"', 
                    'Downloading', 
                    { iconSize: 35, 
                    iconType: 'solid', 
                    position: 'top right' } 
                );
            axios.post(path, null, { params: { songId } })
                .then(() => {
                    this.$refs.alert
                    .showAlert(
                        'success', 
                        'Music successful downloaded', 
                        'Downloaded', 
                        { iconSize: 35, 
                        iconType: 'solid', 
                        position: 'top right' } 
                    );
            })
                .catch((error) => {
                console.error(error);
                this.$refs.alert
                    .showAlert(
                        'error', 
                        'Something went wrong!', 
                        'Error', 
                        { iconSize: 35, 
                        iconType: 'solid', 
                        position: 'top right' }
                    );
            });
            
        }
    },
    components: { RouterLink, VueBasicAlert }
}
</script>

<style>
.search-container {
    max-width: 300px;
    margin: 0 auto;
    padding: 20px;
}

.search-wrapper .song-info {
    width: 180px;

}

.song-info h3, .song-info h4 {
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    text-align: left;
}

.search-input {
    width: 100%;
    height: 2.5rem;
    border: 1px solid #000;
    color: #8693A9;
    border-radius: 2.5rem;
    padding: 20px;
    font-size: 16px;
    background: #DEE7F7;    
    border: 1px solid #eaf5ff;
    filter: drop-shadow(-8px -4px 8px rgba(255, 255, 255, 0.46)) drop-shadow(8px 4px 8px rgba(0, 0, 0, 0.10));
}

.search-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.625rem 1.25rem;
}

.search-cover {
    border-radius: 50%;
    margin-bottom: 2rem;
    border: 2px solid #ECF4FF;
    box-shadow: -15px -15px 15px 0px rgba(255, 255, 255, 0.46), 15px 15px 25px 0px #A9B7CF;
    width: 4rem;
    height: 4rem;
    flex-shrink: 0;
    margin: auto 0;
}
.search-cover img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
}

.download button:disabled {
    filter: grayscale(100%);
    cursor: not-allowed;
}

</style>