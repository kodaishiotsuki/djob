<script setup></script>

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">My jobs</h1>

    <div class="space-y-4">
      <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
        <div>
          <h3 class="mb-2 text-xl font-semibold">title</h3>
          <p class="text-gray-600">job.company_name</p>
        </div>

        <div>
          <p class="mb-2">job.position_location</p>
          <p>job.position_salary</p>
        </div>

        <div>
          <p>Posted job.created_at_formatted</p>
        </div>

        <div class="space-x-4">
          <NuxtLink
            v-bind:to="'/browse/' + 1"
            class="py-4 px-6 bg-teal-700 text-white rounded-xl"
            >Details</NuxtLink
          >
        </div>
      </div>
    </div>
  </div>
</template>
