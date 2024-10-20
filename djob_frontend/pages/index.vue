<script setup></script>

<template>
  <div>
    <div class="py-20 px-6 bg-teal-700 text-center">
      <h1 class="mb-12 text-5xl text-white">Find a job anywhere</h1>

      <NuxtLink
        to="/browse"
        class="inline-block py-4 px-8 bg-teal-900 text-white rounded-xl"
        >Browse</NuxtLink
      >
    </div>

    <div class="py-10 px-6">
      <h2 class="mb-8 text-2xl text-center">Newest jobs</h2>

      <div class="space-y-4">
        <Job />
      </div>
    </div>
  </div>
</template>
