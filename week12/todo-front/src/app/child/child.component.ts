import { Component, OnInit, Output, Input } from '@angular/core';
import { EventEmitter } from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {

  @Input() title='';
  @Output() output = new EventEmitter();

  @Input() numberArray: number []=[];
  @Output() stringArray=new EventEmitter<string[]>();
  constructor() { }

  ngOnInit() {
  }

  
  sendMessage() {
    this.output.emit('Message from Child');
  }

  sendString() {
    this.stringArray.emit(['a','b','c']);
  }

}
