import { Component } from '@angular/core';
import { TaskService } from './services/my_service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Balance Sheet';
  data;
  constructor(private taskService: TaskService) {
    taskService.getTypes().subscribe(types => {
      this.data = types;
    })
  }
}