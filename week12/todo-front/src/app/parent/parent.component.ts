import { Component, OnInit, Input, Output } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ICategory } from '../shared/models/models';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {

  public output = '';
  public stringArray: string []=[];

  public categories: ICategory[] = [];
  public loading = false;

  constructor(private provider: ProviderService) { }

  ngOnInit() {

    this.provider.getCategories().then(res => {
      this.categories = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });
  }

  sendMessageByService(){
    this.provider.sendMessage.emit('This message From Parent Component');
  }

}
