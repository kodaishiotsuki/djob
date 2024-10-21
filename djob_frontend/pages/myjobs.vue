<script setup>
import { onMounted } from "vue";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
const router = useRouter();
let jobs = ref();

onMounted(() => {
  if (!userStore.user.isAuthenticated) {
    router.push({ path: "/login" });
  } else {
    getJobs();
  }
});

async function getJobs() {
  await $fetch("http://127.0.0.1:8000/api/v1/jobs/my/", {
    headers: {
      Authorization: `token ${userStore.user.token}`,
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      jobs.value = response;
    })
    .catch((error) => {
      console.log(error);
    });
}
</script>
<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">My jobs</h1>

    <div class="space-y-4">
      <Job :my="true" v-for="job in jobs" :key="job.id" :job="job" />
    </div>
  </div>
</template>
