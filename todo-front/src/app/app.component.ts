import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService] 
})
export class AppComponent {
   TaskList = [{name: 'test'}];

  constructor(private api: ApiService) {

    this.getTaskList();
  }
  getTaskList = () => { 
    this.api.getAllTaskLists().subscribe(
      data=> {
        this.TaskList=data;
      },
      error => {
        console.log(error)  
      }
    )
   
  }
}
