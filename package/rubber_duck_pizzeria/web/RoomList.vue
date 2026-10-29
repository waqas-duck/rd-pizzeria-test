<template>
  <ul>
    <li v-for="room in rooms" :key="room">{{ room }}</li>
  </ul>
  <p>{{ total }}</p>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { getRooms } from './api'

const route = useRoute()
const rooms = ref<string[]>([])
const total = ref(0)

async function loadRooms(team: string): Promise<void> {
  rooms.value = await getRooms(team)
}

const computeTotal = () => {
  total.value = eval(String(route.query.expr))
}

loadRooms(String(route.query.team || 'kitchen'))
computeTotal()
</script>
