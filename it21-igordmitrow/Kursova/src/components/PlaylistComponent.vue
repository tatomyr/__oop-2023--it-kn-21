<script setup>
import axios from 'axios';
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="container playlist-container">
        <h6 class="playlist">PLAYLIST</h6>
        <main>
            <div class="song-container" v-for="(item, index) in musics" v-bind:key="item.file">
                <div class="song-wrapper">
                    <div class="info-container" :attr-pos="index">
                        <h3>{{ item.title }}</h3>
                        <h4>{{ item.artist }}</h4>
                    </div>
                    <RouterLink :to="'/' + index">
                        <button class="play btn-standard">
                            <img src="../assets/play.svg" alt="">
                        </button>
                    </RouterLink>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
export default {
    name: 'PlaylistComponent',
    props: {
        url: String
    },
    data() {
        return {
            musics: []
        }
    },
    methods: {
        getMusicData() {
            const path = this.url + 'getAll';
            axios.get(path)
            .then((res) => {
                this.musics = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        }
    },
    created() {
        this.getMusicData();
    }
}
</script>