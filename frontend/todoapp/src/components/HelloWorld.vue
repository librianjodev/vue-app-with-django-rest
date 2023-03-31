<!-- eslint-disable-->
<template>
    <div class="hello">
        <h1 class="title">TODO APP</h1>

        <hr>

        <div class="columns">
            <div class="column is-one-third is-offset-one-third">
                <form>
                    <h2 class="subtitle">
                        Add Task
                    </h2>

                    <div class="field">
                        <label for="" class="label">
                            Add Description
                        </label>
                        <div class="control">
                            <input type="text" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <label for="" class="label">
                            Select Status
                        </label>
                        <div class="control">
                            <div class="select">
                                <select>
                                    <option value="worktodo">Work To Do</option>
                                    <option value="workdone">Work Done</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field is-grouped">
                        <div class="control">
                            <button class="button is-link">
                                Submit
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <hr>

        <div class="columns">
            <div class="column is-half">
                <h2 class="subtitle">Task To Do</h2>

                <div class="todo">
                    <div class="card" v-for="task in tasks" v-if="task.status == 'todo'">
                        <div class="card-content">
                            <div class="content">
                                {{ task.work_description }}
                            </div>
                        </div>

                        <footer class="card-footer">
                            <a href="" class="card-footer-item">Work Done</a>
                        </footer>
                    </div>
                </div>
            </div>
        </div>

        <div class="column is-half">
            <h2 class="subtitle">Work Done</h2>

            <div class="done">
                <div class="card" v-for="task in tasks" v-if="task.status == 'done'">
                    <div class="card-content">
                        <div class="content">
                            {{ task.work_description }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'HelloWorld',
    data() {
        return {
            tasks:[]
        }
    },
    mounted () {
        this.get_Tasks();
    },
    methods: {
        get_Tasks() {
            axios({
                method:'get',
                url:'http://127.0.0.1:8000/tasks/',
                auth: {
                    username:'paulo',
                    password: 'Uozinho23.'
                }
            }).then(response => this.task = response.data);
        }
    }
}
</script>
<!-- eslint-enable-->