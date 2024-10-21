<script setup>
import { onMounted } from "vue";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
const router = useRouter();
let jobs = ref();

// コンポーネントがマウントされた際に実行
onMounted(() => {
  if (!userStore.user.isAuthenticated) {
    // ユーザーが認証されていない場合はログインページへリダイレクト
    router.push("/login");
  } else {
    // 認証されている場合は求人情報を取得
    getJobs();
  }
});

async function getJobs() {
  await $fetch("http://127.0.0.1:8000/api/v1/jobs/my", {
    headers: {
      Authorization: "token " + userStore.user.token,
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      jobs.value = response; // 取得した求人情報をjobsに格納
    })
    .catch((error) => {
      console.log("error", error);
    });
}

function deleteJob(id) {
  // jobsから指定されたIDの求人を削除（画面上で削除）
  jobs.value = jobs.value.filter((job) => job.id !== id);
}
</script>

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">My jobs</h1>

    <div class="space-y-4">
      <Job
        v-for="job in jobs"
        :key="job.id"
        :job="job"
        :my="true"
        v-on:deleteJob="deleteJob(job.id)"
      />
    </div>
  </div>
</template>
