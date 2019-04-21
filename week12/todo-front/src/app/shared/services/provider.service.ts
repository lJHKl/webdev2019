import { Injectable, EventEmitter } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ICategory } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) { 
    super(http);
  }
  getCategories(): Promise<ICategory[]>{
    return this.get('http://localhost:8000/api/task_lists/', {}); //Поменять не на категории а под себя в беке
  }
}
